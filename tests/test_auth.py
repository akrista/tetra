from tests.TestCase import TestCase


class TestAuth(TestCase):
    def test_login_page_renders(self):
        self.get("/login").assertOk().assertContains("Sign In")

    def test_register_page_renders(self):
        self.get("/register").assertOk().assertContains("Create account")

    def test_forgot_password_page_renders(self):
        self.get("/password/forgot").assertOk().assertContains("Reset password")

    def test_reset_password_page_renders(self):
        self.get("/password/reset").assertOk().assertContains("Set new password")

    def test_verify_email_page_renders(self):
        self.get("/verify-email").assertOk().assertContains("Check your email")
