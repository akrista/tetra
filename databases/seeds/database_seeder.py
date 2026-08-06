"""Base Database Seeder Module.

Delegates to app.utils.rbac, which owns the single source of truth for the
permission catalog and the TETRA_* env-driven tenant/owner bootstrap.
"""

from masoniteorm.seeds import Seeder

from app.utils.rbac import seed_app_basics


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        seed_app_basics()
