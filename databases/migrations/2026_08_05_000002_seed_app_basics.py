"""Provision app basics on migrate: permissions, default tenant, roles, owner.

The first user comes from TETRA_* env vars so each deployment bootstraps
its own account (see .env-example). Idempotent.
"""

from masoniteorm.migrations import Migration

from app.utils.rbac import seed_app_basics


class SeedAppBasics(Migration):
    def up(self):
        seed_app_basics()

    def down(self):
        # Data migration: nothing structural to roll back.
        pass
