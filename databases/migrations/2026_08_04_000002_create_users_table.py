"""Migration: create users table with tenant columns.

Uses ``INTEGER PRIMARY KEY`` inline because Masonite ORM 3 drops the
table-level ``CONSTRAINT ... PRIMARY KEY`` that ``increments`` generates
when ``compile_create_sql`` runs on SQLite, and SQLite requires the column
itself to be ``INTEGER PRIMARY KEY`` for ``AUTOINCREMENT`` to work.
"""

from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.integer("id", length=11)
            table._last_column.set_as_primary()
            table.string("name", length=255)
            table.string("email", length=255).unique()
            table.string("password", length=255)
            table.string("second_password", length=255).nullable()
            table.string("remember_token", length=255).nullable()
            table.string("phone", length=255).nullable()
            table.timestamp("verified_at").nullable()
            table.unsigned_integer("tenant_id")
            table.foreign("tenant_id").references("id").on("tenants").on_delete(
                "cascade"
            )
            table.boolean("is_owner").default(False)
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")
