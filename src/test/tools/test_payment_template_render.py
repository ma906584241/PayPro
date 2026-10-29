"""Opt-in rendering with the real Thymeleaf libraries from an existing application JAR.

Set PAYPRO_TEST_JAVA_HOME to a JDK 8 installation. No application, database, mail,
Redis or network service is started.
"""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from verify_payment_template import validate_response
sys.path.pop(0)
SPEC = importlib.util.spec_from_file_location("render_fixtures", ROOT / "src/test/tools/test_upgrade_payment_template.py")
FIXTURES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FIXTURES)

JAVA = '''
import java.io.*;
import org.thymeleaf.context.Context;
import org.thymeleaf.spring5.SpringTemplateEngine;
import org.thymeleaf.templateresolver.ClassLoaderTemplateResolver;

public class RenderPayment {
    public static void main(String[] args) throws Exception {
        ClassLoaderTemplateResolver resolver = new ClassLoaderTemplateResolver();
        resolver.setPrefix("templates/");
        resolver.setSuffix(".html");
        resolver.setTemplateMode("HTML");
        resolver.setCharacterEncoding("UTF-8");
        SpringTemplateEngine engine = new SpringTemplateEngine();
        engine.setTemplateResolver(resolver);
        Context context = new Context();
        context.setVariable("name", args[1]);
        context.setVariable("indexTitle", "Test studio");
        context.setVariable("title", "Test studio");
        context.setVariable("supportMail", "test@example.invalid");
        context.setVariable("site", "https://example.invalid");
        context.setVariable("alipayUserId", "test");
        context.setVariable("alipayCustomQrUrl", "");
        context.setVariable("mobile", "");
        try (Writer writer = new OutputStreamWriter(new FileOutputStream(args[0]), "UTF-8")) {
            engine.process("payment", context, writer);
        }
    }
}
'''


@unittest.skipUnless(os.environ.get("PAYPRO_TEST_JAVA_HOME"), "requires an existing JDK and packaged application JAR")
class PaymentTemplateRenderTest(unittest.TestCase):
    def test_runtime_classpath_wins_and_rendered_response_passes_readiness(self):
        with tempfile.TemporaryDirectory(prefix="paypro-render-test-") as tmp:
            base = Path(tmp)
            library = base / "lib"
            library.mkdir()
            application = Path(os.environ.get("PAYPRO_TEST_JAR", str(ROOT / "target/paypro-1.0-SNAPSHOT.jar")))
            with zipfile.ZipFile(application) as archive:
                for member in archive.infolist():
                    if member.filename.startswith("BOOT-INF/lib/") and member.filename.endswith(".jar"):
                        (library / Path(member.filename).name).write_bytes(archive.read(member))
            overlay = base / "config/templates/payment.html"
            overlay.parent.mkdir(parents=True)
            overlay.write_text(FIXTURES.LEGACY, encoding="utf-8")
            runtime = base / "runtime/templates/payment.html"
            prepared = subprocess.run([sys.executable, str(FIXTURES.SCRIPT), "--template", str(overlay),
                                       "--runtime-template", str(runtime), "--apply"], capture_output=True)
            self.assertEqual(prepared.returncode, 0, prepared.stdout + prepared.stderr)
            # A later restore must not replace this process's already prepared template.
            overlay.write_text(FIXTURES.LEGACY, encoding="utf-8")
            source = base / "RenderPayment.java"
            source.write_text(JAVA, encoding="utf-8")
            classpath = os.pathsep.join(str(path) for path in (base / "runtime", base / "config", base, library / "*"))
            java_bin = Path(os.environ["PAYPRO_TEST_JAVA_HOME"]) / "bin"
            suffix = ".exe" if os.name == "nt" else ""
            compiled = subprocess.run([str(java_bin / ("javac" + suffix)), "-encoding", "UTF-8", "-cp", classpath,
                                       str(source)], capture_output=True, timeout=30)
            self.assertEqual(compiled.returncode, 0, compiled.stdout + compiled.stderr)
            page = base / "rendered.html"
            rendered = subprocess.run([str(java_bin / ("java" + suffix)), "-cp", classpath, "RenderPayment",
                                       str(page), "AI智为工作室"], capture_output=True, timeout=30)
            self.assertEqual(rendered.returncode, 0, rendered.stdout + rendered.stderr)
            validate_response(page.read_text(encoding="utf-8"), FIXTURES.CANONICAL, "AI智为工作室")


if __name__ == "__main__":
    unittest.main()
