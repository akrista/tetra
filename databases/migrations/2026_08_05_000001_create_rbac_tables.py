"""Roles, permissions and their pivot tables for tenant-scoped RBAC."""

from masoniteorm.migrations import Migration


class CreateRbacTables(Migration):
    def up(self):
        with self.schema.create("roles") as table:
            table.integer("id", length=11)
            table._last_column.set_as_primary()
            table.string("name", length=120)
            table.string("slug", length=60)
            table.unsigned_integer("tenant_id")
            table.foreign("tenant_id").references("id").on("tenants").on_delete(
                "cascade"
            )
            table.unique(["tenant_id", "slug"])
            table.timestamps()

        with self.schema.create("permissions") as table:
            table.integer("id", length=11)
            table._last_column.set_as_primary()
            table.string("slug", length=60).unique()
            table.string("name", length=120)
            table.timestamps()

        with self.schema.create("permission_role") as table:
            table.integer("id", length=11)
            table._last_column.set_as_primary()
            table.integer("role_id")
            table.integer("permission_id")
            table.foreign("role_id").references("id").on("roles").on_delete("cascade")
            table.foreign("permission_id").references("id").on("permissions").on_delete(
                "cascade"
            )
            table.unique(["role_id", "permission_id"])

        with self.schema.create("role_user") as table:
            table.integer("id", length=11)
            table._last_column.set_as_primary()
            table.integer("user_id")
            table.integer("role_id")
            table.foreign("user_id").references("id").on("users").on_delete("cascade")
            table.foreign("role_id").references("id").on("roles").on_delete("cascade")
            table.unique(["user_id", "role_id"])

    def down(self):
        self.schema.drop_table("role_user")
        self.schema.drop_table("permission_role")
        self.schema.drop_table("permissions")
        self.schema.drop_table("roles")
