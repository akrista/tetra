from app.models.User import User
from tests.TestCase import TestCase


class TestProfile(TestCase):
    def test_profile_page_renders_all_sections(self):
        user = self.make_user(email="profile@example.com")
        self.actingAs(user)
        self.get("/profile").assertOk().assertContains("Datos")
        self.get("/profile").assertContains("Contraseña")
        self.get("/profile").assertContains("Correo")

    def test_update_name_and_phone(self):
        user = self.make_user(email="update@example.com")
        self.actingAs(user)
        res = self.post("/profile", {"name": "Nuevo Nombre", "phone": "+582121234567"})
        res.assertRedirect()
        fresh = User.find(user.id)
        self.assertEqual(fresh.name, "Nuevo Nombre")
        self.assertEqual(fresh.phone, "+582121234567")

    def test_password_change_success(self):
        from masonite.facades import Hash

        user = self.make_user(email="pw@example.com")
        self.actingAs(user)
        res = self.post(
            "/profile/password",
            {
                "current_password": "password1234",
                "password": "nuevapass1",
                "password_confirmation": "nuevapass1",
            },
        )
        res.assertRedirect()
        fresh = User.find(user.id)
        self.assertTrue(Hash.check("nuevapass1", fresh.password))

    def test_password_change_wrong_current(self):
        from masonite.facades import Hash

        user = self.make_user(email="pw2@example.com")
        self.actingAs(user)
        res = self.post(
            "/profile/password",
            {
                "current_password": "incorrecta",
                "password": "nuevapass1",
                "password_confirmation": "nuevapass1",
            },
        )
        res.assertRedirect()
        fresh = User.find(user.id)
        self.assertTrue(Hash.check("password1234", fresh.password))

    def test_password_change_short_password(self):
        from masonite.facades import Hash

        user = self.make_user(email="pw3@example.com")
        self.actingAs(user)
        res = self.post(
            "/profile/password",
            {
                "current_password": "password1234",
                "password": "corta",
                "password_confirmation": "corta",
            },
        )
        res.assertRedirect()
        fresh = User.find(user.id)
        self.assertTrue(Hash.check("password1234", fresh.password))

    def test_password_change_rotates_remember_token(self):
        user = self.make_user(email="pwrot@example.com")
        user.set_remember_token()
        user.save()
        old_token = user.remember_token
        self.actingAs(user)
        res = self.post(
            "/profile/password",
            {
                "current_password": "password1234",
                "password": "nuevapass1",
                "password_confirmation": "nuevapass1",
            },
        )
        res.assertRedirect()
        fresh = User.find(user.id)
        self.assertNotEqual(fresh.remember_token, old_token)

    def test_email_change_success(self):
        user = self.make_user(email="old@example.com")
        self.actingAs(user)
        res = self.post(
            "/profile/email",
            {"email": "new@example.com", "current_password": "password1234"},
        )
        res.assertRedirect()
        fresh = User.where("email", "new@example.com").first()
        self.assertIsNotNone(fresh)
        self.assertIsNone(User.where("email", "old@example.com").first())

    def test_email_change_duplicate(self):
        user = self.make_user(email="owner@example.com")
        self.make_user(
            tenant=user.tenant, name="Otra", email="taken@example.com", owner=False
        )
        self.actingAs(user)
        res = self.post(
            "/profile/email",
            {"email": "taken@example.com", "current_password": "password1234"},
        )
        res.assertRedirect()
        self.assertIsNotNone(User.where("email", "owner@example.com").first())

    def test_email_change_wrong_password(self):
        user = self.make_user(email="pwcheck@example.com")
        self.actingAs(user)
        res = self.post(
            "/profile/email",
            {"email": "hacked@example.com", "current_password": "incorrecta"},
        )
        res.assertRedirect()
        self.assertIsNotNone(User.where("email", "pwcheck@example.com").first())
        self.assertIsNone(User.where("email", "hacked@example.com").first())
