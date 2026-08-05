"""Migration: create tenants table."""

from masoniteorm.migrations import Migration


class CreateTenantsTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("tenants") as table:
            table.increments("id")
            table.string("name", length=120)
            table.string("slug", length=60).unique()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("tenants")
