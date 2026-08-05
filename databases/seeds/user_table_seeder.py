"""UserTableSeeder Seeder — one owner in the Acme tenant."""

from masonite.facades import Hash
from masoniteorm.seeds import Seeder

from app.models.Tenant import Tenant
from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        tenant = Tenant.where("slug", "acme").first()
        if not tenant:
            return

        User.first_or_create(
            {"email": "owner@acme.test"},
            {
                "name": "Acme Owner",
                "password": Hash.make("password1234"),
                "tenant_id": tenant.id,
                "is_owner": True,
                "verified_at": "2026-01-01 00:00:00",
            },
        )
