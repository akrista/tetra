"""Set request._tenant for the current request, defensively re-asserting from the user record."""

from masonite.middleware import Middleware
from masoniteorm.exceptions import QueryException


class TenantContextMiddleware(Middleware):
    def before(self, request, response):
        user = request.user()
        if not user:
            request._tenant = None
            return request

        session_tenant_id = request.session.get("tenant_id")
        if session_tenant_id is not None and session_tenant_id != user.tenant_id:
            request.session.set("tenant_id", user.tenant_id)

        try:
            request._tenant = user.tenant
        except QueryException:
            request._tenant = None
        return request

    def after(self, request, response):
        return request
