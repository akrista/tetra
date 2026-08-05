from app.models.Role import Role
from tests.TestCase import TestCase


class TestRoles(TestCase):
    def test_roles_index_requires_permission(self):
        tenant = self.make_tenant()
        member = self.make_user(
            tenant=tenant, email="noaccess@example.com", owner=False
        )
        self.actingAs(member)
        self.get("/roles").assertRedirect()

    def test_roles_index_shows_roles(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.make_role(tenant=tenant, name="Editor", permissions=["users.manage"])
        self.actingAs(owner)
        self.get("/roles").assertOk().assertContains("Editor").assertContains(
            "users.manage"
        )

    def test_member_cannot_edit_role_with_unheld_permissions(self):
        tenant = self.make_tenant()
        self.make_user(tenant=tenant, email="owner@example.com")
        admin_role = self.make_role(
            tenant=tenant, name="Admin", permissions=["users.manage", "roles.manage"]
        )
        gestor = self.make_role(
            tenant=tenant, name="Gestor", permissions=["roles.manage"]
        )
        staff = self.make_user(tenant=tenant, email="staff@example.com", owner=False)
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": staff.id, "role_id": gestor.id})
        self.actingAs(staff)
        res = self.post(
            f"/roles/{admin_role.id}",
            {"name": "Admin Modificado", "permissions": ["roles.manage"]},
        )
        res.assertRedirect()
        self.assertEqual(Role.find(admin_role.id).name, "Admin")

    def test_roles_create_page_renders(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.actingAs(owner)
        self.get("/roles/create").assertOk().assertContains("Gestionar usuarios")

    def test_roles_store_creates_role_with_permissions(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.actingAs(owner)
        res = self.post(
            "/roles",
            {"name": "Auditor", "permissions": ["users.manage"]},
        )
        res.assertRedirect()
        role = Role.where("slug", "auditor").first()
        self.assertIsNotNone(role)
        builder = self.application.make("builder").new().table("permission_role")
        row = builder.where("role_id", role.id).first()
        self.assertIsNotNone(row)
        self.assertNotEqual(row["permission_id"], None)

    def test_roles_store_duplicate_name_fails(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        self.make_role(tenant=tenant, name="Editor")
        self.actingAs(owner)
        res = self.post("/roles", {"name": "Editor", "permissions": []})
        res.assertRedirect()
        self.assertEqual(Role.where("slug", "editor").count(), 1)

    def test_roles_edit_cross_tenant_is_forbidden(self):
        tenant_a = self.make_tenant(name="Alpha")
        tenant_b = self.make_tenant(name="Beta")
        owner = self.make_user(tenant=tenant_a, email="owner@alpha.com")
        victim_role = self.make_role(tenant=tenant_b, name="Secreto")
        self.actingAs(owner)
        self.get(f"/roles/{victim_role.id}/edit").assertRedirect()

    def test_roles_update_syncs_permissions(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        role = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        self.actingAs(owner)
        res = self.post(
            f"/roles/{role.id}",
            {"name": "Editor Plus", "permissions": ["roles.manage"]},
        )
        res.assertRedirect()
        fresh = Role.find(role.id)
        self.assertEqual(fresh.name, "Editor Plus")
        builder = self.application.make("builder").new().table("permission_role")
        rows = builder.where("role_id", role.id).get()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["permission_id"], 2)

    def test_roles_delete_blocked_when_assigned(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        role = self.make_role(
            tenant=tenant, name="Editor", permissions=["users.manage"]
        )
        staff = self.make_user(tenant=tenant, email="staff@example.com", owner=False)
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": staff.id, "role_id": role.id})
        self.actingAs(owner)
        res = self.post(f"/roles/{role.id}/delete", {})
        res.assertRedirect()
        self.assertIsNotNone(Role.find(role.id))

    def test_roles_delete_unassigned(self):
        tenant = self.make_tenant()
        owner = self.make_user(tenant=tenant, email="owner@example.com")
        role = self.make_role(tenant=tenant, name="Vacio")
        self.actingAs(owner)
        res = self.post(f"/roles/{role.id}/delete", {})
        res.assertRedirect()
        self.assertIsNone(Role.find(role.id))

    def test_member_cannot_grant_permission_they_lack(self):
        tenant = self.make_tenant()
        role = self.make_role(
            tenant=tenant, name="GestorRoles", permissions=["roles.manage"]
        )
        staff = self.make_user(tenant=tenant, email="staff@example.com", owner=False)
        builder = self.application.make("builder").new()
        builder.table("role_user").create({"user_id": staff.id, "role_id": role.id})
        self.actingAs(staff)
        res = self.post(
            "/roles",
            {"name": "Escalado", "permissions": ["users.manage"]},
        )
        res.assertRedirect()
        new_role = Role.where("slug", "escalado").first()
        self.assertIsNotNone(new_role)
        rows = (
            self.application.make("builder")
            .new()
            .table("permission_role")
            .where("role_id", new_role.id)
            .get()
        )
        self.assertEqual(len(rows), 0)
