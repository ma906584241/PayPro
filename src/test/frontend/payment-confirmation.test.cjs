// Runs the real payment-page component with fake network/timers; never sends email.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const html = fs.readFileSync(path.resolve(__dirname, '../../main/resources/templates/payment.html'), 'utf8');
const source = html.match(/<script th:inline="javascript">([\s\S]*?)<\/script>/)[1];
const pending = () => ({orderState:0, amount:9.90, payType:'alipay', payNum:'1234', expireTime:null,
    confirmedAt:null, noticeStatus:'NOT_REQUESTED', canConfirm:true, retryable:false});

function harness({legacy=false, accept=true, data=pending(), errorCode}={}) {
    const calls = {get:[], post:[], dialogs:0};
    const intervals = new Map();
    let state = data, component, timerId=0, app;
    const context = {
        console, URLSearchParams, Date, QRCode:{},
        window:{location:{search:'?orderId=test&payType=alipay&money=1'+(legacy?'':'&paymentConfirmToken=payer-token')},
            confirm(){ calls.dialogs++; return accept; }},
        document:{getElementById(){return null;}},
        API_CONFIG:{ENDPOINTS:{PAYMENT_CONFIRMATION:'/order/payment-confirmation', CONFIRM_PAID:'/order/confirm-paid', STATUS:'/order/state'}},
        setTimeout(fn){fn();return 1;},
        setInterval(fn,ms){intervals.set(++timerId,{fn,ms});return timerId;},
        clearInterval(id){intervals.delete(id);},
        getHttpUtil(){ return {async request(url,options){calls.get.push({url,options}); return errorCode ? {code:errorCode,msg:'invalid'} : {code:200,data:{...state}};}}; },
        async getRequest(url){calls.get.push({url});return {code:200,data:0};},
        async postRequest(url,body){ calls.post.push({url,body}); state={...state,confirmedAt:'2026-10-28T12:00:00Z',noticeStatus:'SENDING',canConfirm:false,retryable:false}; return {code:200,data:{...state}}; },
        Vue:{ createApp(options){component=options;return {mount(){}};} }
    };
    vm.runInNewContext(source,context,{filename:'payment.html'});
    app=component.data();
    app.$nextTick=async()=>{};
    for(const [name,method] of Object.entries(component.methods)) app[name]=method.bind(app);
    for(const [name,getter] of Object.entries(component.computed)) Object.defineProperty(app,name,{get:getter.bind(app)});
    return {app,calls,intervals, async mount(){await app.initPayment();},
        setState(next){state=next;}, unmount(){component.beforeUnmount.call(app);}};
}

test('opening, polling, reloading and cancelling confirmation never POST',async()=>{
    const h=harness({accept:false}); await h.mount();
    assert.equal(h.app.orderInfo.actualAmount,'9.90');
    assert.equal(h.calls.post.length,0);
    await h.app.confirmPaid();
    assert.equal(h.calls.dialogs,1); assert.equal(h.calls.post.length,0);
    for(const timer of h.intervals.values()) if(timer.ms===2000) await timer.fn();
    assert.equal(h.calls.post.length,0);
    assert.equal(h.calls.get[0].options.headers['X-Payment-Confirm-Token'],'payer-token');
    const reload=harness();await reload.mount(); assert.equal(reload.calls.post.length,0);
});

test('explicit confirmation posts once, remains pending review and keeps polling',async()=>{
    const h=harness();await h.mount();await h.app.confirmPaid();
    assert.equal(h.calls.post.length,1);assert.equal(h.app.paymentStatus,'pending');
    assert.equal(h.app.reportedPaid,true);assert.equal(h.app.showCountdown,false);
    assert.equal([...h.intervals.values()].some(t=>t.ms===2000),true);
    await h.app.confirmPaid();assert.equal(h.calls.post.length,1);
    h.setState({...pending(),confirmedAt:'2026-10-28',noticeStatus:'SENT',canConfirm:false});
    await h.app.refreshConfirmationStatus();await h.app.confirmPaid();assert.equal(h.calls.post.length,1);
    h.setState({...pending(),orderState:1,canConfirm:false});await h.app.refreshConfirmationStatus();
    assert.equal(h.app.paymentStatus,'success');assert.equal(h.intervals.size,0);
});

test('failed email can be retried without asking the customer to pay again',async()=>{
    const h=harness({data:{...pending(),confirmedAt:'2026-10-28',noticeStatus:'FAILED',canConfirm:true,retryable:true}});
    await h.mount();assert.equal(h.app.canReportPaid,true);assert.equal(h.calls.post.length,0);
    await h.app.confirmPaid();assert.equal(h.calls.post.length,1);assert.equal(h.calls.dialogs,0);
    assert.equal(h.app.paymentStatus,'pending');assert.equal(h.app.showCountdown,false);
});

test('legacy links do not use the confirmation endpoints',async()=>{
    const h=harness({legacy:true});await h.mount();await h.app.confirmPaid();
    assert.equal(h.app.hasConfirmToken,false);assert.equal(h.app.canReportPaid,false);
    assert.equal(h.calls.get.length,0);assert.equal(h.calls.post.length,0);
});

test('invalid credentials disable confirmation, QR display and polling',async()=>{
    const h=harness({errorCode:403});await h.mount();await h.app.confirmPaid();
    assert.equal(h.app.confirmationInvalid,true);assert.equal(h.app.confirmationInfo,null);
    assert.equal(h.app.canReportPaid,false);assert.equal(h.calls.post.length,0);assert.equal(h.intervals.size,0);
});

test('refresh restores review state and does not create a fictitious five-minute expiry',async()=>{
    const h=harness();await h.mount();assert.equal(h.app.showCountdown,false);
    assert.equal([...h.intervals.values()].some(t=>t.ms===1000),false);
    const restored=harness({data:{...pending(),confirmedAt:'2026-10-28',noticeStatus:'SENT',canConfirm:false}});
    await restored.mount();assert.equal(restored.app.reportedPaid,true);assert.equal(restored.calls.post.length,0);
    restored.unmount();assert.equal(restored.intervals.size,0);
});

test('terminal server state blocks confirmation',async()=>{
    for(const state of [1,2,5]){
        const h=harness({data:{...pending(),orderState:state,canConfirm:false}});
        await h.mount();await h.app.confirmPaid();assert.equal(h.calls.post.length,0);
        assert.equal(h.app.canReportPaid,false);assert.equal(h.intervals.size,0);
    }
});
