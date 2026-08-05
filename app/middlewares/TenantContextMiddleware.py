"""Re-assert session tenant_id from the user record."""

from masonite.middleware import Middleware


class TenantContextMiddleware(Middleware):
    def before(self, request, response):
        user = request.user()
        if not user:
            return request

        session_tenant_id = request.session.get("tenant_id")
        if session_tenant_id is not None and session_tenant_id != user.tenant_id:
            request.session.set("tenant_id", user.tenant_id)
        return request

    def after(self, request, response):
        return request
