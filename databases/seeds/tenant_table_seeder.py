"""Seed one tenant so the Evidence Collector can log in manually."""

from masoniteorm.seeds import Seeder

from app.models.Tenant import Tenant


class TenantTableSeeder(Seeder):
    def run(self):
        Tenant.first_or_create(
            {"slug": "acme"},
            {"name": "Acme Workspace"},
        )
