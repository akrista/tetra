from tests.TestCase import TestCase


class TestErrors(TestCase):
    def test_404_template_renders(self):
        content = self.application.make("view").render("errors/404").get_content()
        self.assertIn("No encontrado", content)
        self.assertIn("404", content)

    def test_403_template_renders(self):
        content = self.application.make("view").render("errors/403").get_content()
        self.assertIn("Prohibido", content)
        self.assertIn("403", content)

    def test_500_template_renders(self):
        content = self.application.make("view").render("errors/500").get_content()
        self.assertIn("Error del servidor", content)
        self.assertIn("500", content)

    def test_503_template_renders(self):
        content = self.application.make("view").render("errors/503").get_content()
        self.assertIn("Servicio no disponible", content)
        self.assertIn("503", content)
