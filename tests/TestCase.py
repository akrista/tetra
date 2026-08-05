from datetime import UTC, datetime

from masonite.facades import Hash
from masonite.tests import TestCase as MasoniteTestCase

from app.models.Tenant import Tenant
from app.models.User import User


class TestCase(MasoniteTestCase):
    def setUp(self):
        super().setUp()
        # ponytail: wipe the relevant tables between tests so slug/email
        # uniqueness doesn't bleed across tests. Faster than re-migrating.
        # Best-effort: missing tables are fine on the first test before any
        # migration has run.
        builder = self.application.make("builder").new()
        for table in ("password_resets", "users", "tenants", "notifications"):
            try:
                builder.table(table).delete()
            except Exception:  # noqa: BLE001, S110
                pass

    def make_tenant(self, name="Acme Workspace", slug=None):
        from app.utils.slug import slugify

        if slug is None:
            slug = slugify(name)
        return Tenant.create({"name": name, "slug": slug})

    def make_user(
        self,
        tenant=None,
        name="Test User",
        email="user@example.com",
        password="password1234",
        owner=True,
        verified=True,
    ):
        if tenant is None:
            tenant = self.make_tenant()
        return User.create(
            {
                "name": name,
                "email": email,
                "password": Hash.make(password),
                "tenant_id": tenant.id,
                "is_owner": owner,
                "verified_at": datetime.now(UTC).isoformat(sep=" ")
                if verified
                else None,
            }
        )

    def login_as(self, user):
        self.post("/login", {"email": user.email, "password": "password1234"})
