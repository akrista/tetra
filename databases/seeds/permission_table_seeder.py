"""Seed the global permission catalog (safe to re-run)."""

from masoniteorm.seeds import Seeder

from app.models.Permission import Permission

PERMISSIONS = [
    ("users.manage", "Gestionar usuarios"),
    ("roles.manage", "Gestionar roles"),
]


class PermissionTableSeeder(Seeder):
    def run(self):
        for slug, name in PERMISSIONS:
            Permission.first_or_create({"slug": slug}, {"name": name})
