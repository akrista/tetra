from app.models.User import User
from tests.TestCase import TestCase


class TestUsers(TestCase):
    def test_users_index_requires_permission(self):
        tenant = self.make_tenant()
        member = self.make_user(
            tenant=tenant, email="noaccess@example.com", owner=False
        )
        self.actingAs(member)
        self.get("/users").assertRedirect()

    def test_users_index_lists_only_own_tenant(self):
        tenant_a = self.make_tenant(name="Alpha")
        tenant_b = self.make_tenant(name="Beta")
        owner = self.make_user(tenant=tenant_a, email="owner@alpha.com")
        self.make_user(
            tenant=tenant_a, name="Visible", email="vis@alpha.com", owner=False
        )
        self.make_user(
            tenant=tenant_b, name="Invisible", email="inv@beta.com", owner=False
        )
        self.actingAs(owner)
        self.get("/users").assertOk().assertContains("Visible")
        self.get("/users").assertNotContains("Invisible")

    def test_users_create_page_renders(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.actingAs(owner)
        self.get("/users/create").assertOk().assertContains("Nuevo usuario")

    def test_users_store_creates_user_with_role(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        role = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        self.actingAs(owner)
        res = self.post(
            "/users",
            {
                "name": "Nuevo Miembro",
                "email": "nuevo@example.com",
                "phone": "0412-555-1212",
                "password": "password1234",
                "password_confirmation": "password1234",
                "role_id": str(role.id),
            },
        )
        res.assertRedirect()
        new_user = User.where("email", "nuevo@example.com").first()
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user.phone, "0412-555-1212")
        builder = self.application.make("builder").new().table("role_user")
        row = builder.where("user_id", new_user.id).first()
        self.assertIsNotNone(row)
        self.assertEqual(row["role_id"], role.id)

    def test_users_store_duplicate_email_fails(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.make_user(tenant=tenant, email="taken@example.com", owner=False)
        self.actingAs(owner)
        res = self.post(
            "/users",
            {
                "name": "Otro",
                "email": "taken@example.com",
                "password": "password1234",
                "password_confirmation": "password1234",
            },
        )
        res.assertRedirect()
        self.assertEqual(User.where("email", "taken@example.com").count(), 1)

    def test_users_store_short_password_fails(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.actingAs(owner)
        res = self.post(
            "/users",
            {
                "name": "Corto",
                "email": "corto@example.com",
                "password": "corta",
                "password_confirmation": "corta",
            },
        )
        res.assertRedirect()
        self.assertIsNone(User.where("email", "corto@example.com").first())

    def test_users_edit_cross_tenant_is_forbidden(self):
        tenant_a = self.make_tenant(name="Alpha")
        tenant_b = self.make_tenant(name="Beta")
        owner = self.make_user(tenant=tenant_a, email="owner@alpha.com")
        victim = self.make_user(tenant=tenant_b, email="victim@beta.com")
        self.actingAs(owner)
        self.get(f"/users/{victim.id}/edit").assertRedirect()

    def test_users_edit_page_preselects_role(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        member = self.make_user(tenant=tenant, email="member@example.com", owner=False)
        role = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": member.id, "role_id": role.id})
        self.actingAs(owner)
        self.get(f"/users/{member.id}/edit").assertOk().assertContains(
            f'value="{role.id}" selected'
        )

    def test_member_cannot_edit_owner(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        role = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        staff = self.make_user(tenant=tenant, email="staff@example.com", owner=False)
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": staff.id, "role_id": role.id})
        self.actingAs(staff)
        res = self.post(
            f"/users/{owner.id}",
            {"name": "Hackeado", "email": "hacked@example.com", "role_id": ""},
        )
        res.assertRedirect()
        self.assertEqual(User.find(owner.id).email, "owner@example.com")

    def test_member_cannot_self_assign_powerful_role(self):
        tenant = self.make_tenant()
        self.make_user(tenant=tenant, email="owner@example.com")
        editor = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        admin = self.make_role(
            tenant=tenant, name="Admin", permissions=["users.manage", "roles.manage"]
        )
        staff = self.make_user(tenant=tenant, email="staff@example.com", owner=False)
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": staff.id, "role_id": editor.id})
        self.actingAs(staff)
        res = self.post(
            f"/users/{staff.id}",
            {"name": staff.name, "email": staff.email, "role_id": str(admin.id)},
        )
        res.assertRedirect()
        rows = (
            self.application.make("builder")
            .new()
            .table("role_user")
            .where("user_id", staff.id)
            .get()
        )
        self.assertEqual(len(rows), 0)

    def test_users_update(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        member = self.make_user(tenant=tenant, email="member@example.com", owner=False)
        self.actingAs(owner)
        res = self.post(
            f"/users/{member.id}",
            {"name": "Renombrado", "email": "renombrado@example.com", "role_id": ""},
        )
        res.assertRedirect()
        fresh = User.find(member.id)
        self.assertEqual(fresh.name, "Renombrado")
        self.assertEqual(fresh.email, "renombrado@example.com")

    def test_users_delete_self_blocked(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.actingAs(owner)
        res = self.post(f"/users/{owner.id}/delete", {})
        res.assertRedirect()
        self.assertIsNotNone(User.find(owner.id))

    def test_users_delete_last_owner_blocked(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="solo@example.com")
        self.actingAs(owner)
        self.post(f"/users/{owner.id}/delete", {})
        self.assertIsNotNone(User.find(owner.id))

    def test_users_delete_member(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        member = self.make_user(tenant=tenant, email="bye@example.com", owner=False)
        self.actingAs(owner)
        res = self.post(f"/users/{member.id}/delete", {})
        res.assertRedirect()
        self.assertIsNone(User.find(member.id))

    def test_member_with_users_permission_can_manage(self):
        tenant = self.make_tenant()
        role = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        staff = self.make_user(tenant=tenant, email="staff@example.com", owner=False)
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": staff.id, "role_id": role.id})
        self.actingAs(staff)
        self.get("/users").assertOk()
        self.get("/users/create").assertOk()
        res = self.post(
            "/users",
            {
                "name": "De Staff",
                "email": "de-staff@example.com",
                "password": "password1234",
                "password_confirmation": "password1234",
            },
        )
        res.assertRedirect()
        self.assertIsNotNone(User.where("email", "de-staff@example.com").first())
