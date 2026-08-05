"""Migration: rebuild users table with proper PRIMARY KEY and tenant columns.

The Masonite ORM 3 ``Blueprint.increments`` method adds a table-level
``CONSTRAINT ... PRIMARY KEY`` clause, but the SQLite platform drops it
when ``compile_create_sql`` runs. SQLite requires the column itself to be
``INTEGER PRIMARY KEY`` for ``AUTOINCREMENT`` to work, so we rebuild the
table with the primary key inline. This migration must run after
``add_tenant_columns_to_users_table`` so it picks up ``tenant_id`` and
``is_owner``. This is a no-op for the auth milestone because we always
start with an empty database.
"""

from masoniteorm.migrations import Migration


class RebuildUsersTableWithPrimaryKey(Migration):
    def up(self):
        self.schema.drop_table("users")
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
        self.schema.drop_table("users")
