"""Migration: add tenant_id, is_owner to users."""

from masoniteorm.migrations import Migration


class AddTenantColumnsToUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.table("users") as table:
            table.unsigned_integer("tenant_id")
            table.foreign("tenant_id").references("id").on("tenants").on_delete(
                "cascade"
            )
            table.boolean("is_owner").default(False)
            table.index("tenant_id")

    def down(self):
        """Revert the migrations."""
        with self.schema.table("users") as table:
            table.drop_column("is_owner")
            table.drop_foreign("users_tenant_id_foreign")
            table.drop_column("tenant_id")
