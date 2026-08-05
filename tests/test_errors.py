from tests.TestCase import TestCase


class TestErrors(TestCase):
    def test_404_template_renders(self):
        content = self.application.make("view").render("errors/404").get_content()
        self.assertIn("Page Not Found", content)
        self.assertIn("404", content)
        self.assertIn("Go Home", content)
        self.assertIn("/static/svg/404.svg", content)

    def test_403_template_renders(self):
        content = self.application.make("view").render("errors/403").get_content()
        self.assertIn("Forbidden", content)
        self.assertIn("403", content)
        self.assertIn("/static/svg/403.svg", content)

    def test_500_template_renders(self):
        content = self.application.make("view").render("errors/500").get_content()
        self.assertIn("Server Error", content)
        self.assertIn("500", content)
        self.assertIn("/static/svg/500.svg", content)

    def test_503_template_renders(self):
        content = self.application.make("view").render("errors/503").get_content()
        self.assertIn("Service Unavailable", content)
        self.assertIn("503", content)
        self.assertIn("/static/svg/503.svg", content)
