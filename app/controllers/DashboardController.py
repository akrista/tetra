"""Post-login landing page for the tenant workspace."""

from datetime import UTC, datetime

from masonite.controllers import Controller
from masonite.request import Request
from masonite.views import View

from app.models.Role import Role
from app.models.User import User


class DashboardController(Controller):
    def show(self, request: Request, view: View):
        user = request.user()

        hour = datetime.now(UTC).hour
        if hour < 12:
            greeting = "Buenos días"
        elif hour < 19:
            greeting = "Buenas tardes"
        else:
            greeting = "Buenas noches"

        role_names = user.role_names()
        role_label = (
            "Dueño" if user.is_owner else (role_names[0] if role_names else "Miembro")
        )

        return view.render(
            "app.dashboard",
            {
                "user": user,
                "tenant": user.tenant,
                "greeting": greeting,
                "role_label": role_label,
                "users_count": User.where("tenant_id", user.tenant_id).count(),
                "roles_count": Role.where("tenant_id", user.tenant_id).count(),
                "active_page": "dashboard",
            },
        )
