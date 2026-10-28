package com.wendao.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.wendao.entity.Order;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Param;

import java.math.BigDecimal;
import java.util.Date;
import java.util.List;

/**
 * @author lld
 */
public interface OrderMapper extends BaseMapper<Order> {

    @Update("UPDATE t_order SET payment_confirmed_at = COALESCE(payment_confirmed_at, #{now}), " +
            "admin_notice_status = 'SENDING', update_time = #{now} " +
            "WHERE id = #{id} AND payment_confirm_token_hash = #{hash} " +
            "AND state IN (0, 4) " +
            "AND (payment_confirmed_at IS NOT NULL OR expire_time IS NULL OR expire_time >= #{now}) " +
            "AND (admin_notice_status IS NULL OR admin_notice_status <> 'SENT')")
    int claimPaymentNotice(@Param("id") String id, @Param("hash") String hash, @Param("now") Date now);

    @Update("UPDATE t_order SET admin_notice_status = #{status}, update_time = NOW() " +
            "WHERE id = #{id} AND admin_notice_status = 'SENDING'")
    int finishPaymentNotice(@Param("id") String id, @Param("status") String status);

    @Update("UPDATE t_order SET state = 1, update_time = NOW() WHERE id = #{id} AND state IN (0, 4)")
    int approveOrder(@Param("id") String id);

    @Select("select * from t_order where state = #{state} "
            + "and ((expire_time is not null and expire_time < now()) "
            + "or (expire_time is null and create_time < #{expireTime}))")
    List<Order> getExpiredOrders(Integer state, Date expireTime);

    @Select(value = "select sum(money) from t_order where state = 1")
    BigDecimal countAllMoney();

    @Select(value = "select sum(money) from t_order where state = 1 and pay_type = #{payType}")
    BigDecimal countAllMoneyByType(String payType);

    @Select(value = "select sum(money) from t_order where state = 1 and create_time between #{date1} and #{date2}")
    BigDecimal countMoney(Date date1, Date date2);

    @Select(value = "select sum(money) from t_order where state = 1 and pay_type = #{payType} and create_time between #{date1} and #{date2}")
    BigDecimal countMoneyByType(String payType, Date date1, Date date2);

    /**
     * 根据实际金额和时间窗口查找减额模式订单(用于自动匹配)
     */
    @Select("SELECT * FROM t_order WHERE actual_amount = #{actualAmount} " +
            "AND match_mode = 'DECREMENT' " +
            "AND state IN (0, 4) " +
            "AND create_time BETWEEN #{startTime} AND #{endTime} " +
            "ORDER BY create_time ASC LIMIT 1")
    Order getDecrementOrderByAmount(BigDecimal actualAmount, Date startTime, Date endTime);
}
