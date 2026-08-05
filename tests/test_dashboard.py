from tests.TestCase import TestCase


class TestDashboard(TestCase):
    def test_dashboard_requires_auth(self):
        self.get("/dashboard").assertRedirect()

    def test_dashboard_shows_tenant_greeting_and_owner_badge(self):
        tenant = self.make_tenant(name="Acme Workspace")
        user = self.make_user(tenant=tenant, name="Ana Pérez", email="ana@example.com")
        self.actingAs(user)
        self.get("/dashboard").assertOk().assertContains("Acme Workspace")
        self.get("/dashboard").assertContains("Buen")
        self.get("/dashboard").assertContains("Dueño")

    def test_dashboard_shows_counts(self):
        tenant = self.make_tenant(name="Counts")
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.make_user(
            tenant=tenant, name="Miembro", email="m@example.com", owner=False
        )
        self.make_role(tenant=tenant, name="Editor", permissions=["users.manage"])
        self.actingAs(owner)
        self.get("/dashboard").assertOk().assertContains("Usuarios en el equipo")
        self.get("/dashboard").assertContains("Roles definidos")

    def test_dashboard_unverified_shows_banner(self):
        tenant = self.make_tenant()
        user = self.make_user(tenant=tenant, email="nov@example.com", verified=False)
        self.actingAs(user)
        self.get("/dashboard").assertOk().assertContains("Verifica tu correo")

    def test_member_without_permissions_sees_profile_only(self):
        tenant = self.make_tenant()
        member = self.make_user(tenant=tenant, email="member@example.com", owner=False)
        self.actingAs(member)
        self.get("/dashboard").assertOk().assertContains("Ir a mi perfil")
        self.get("/dashboard").assertNotContains('href="/users"')
