"""Route middleware that gates a route behind a permission slug.

Usage: route.middleware("permission:users.manage"). Owner bypasses all checks.
"""

from masonite.middleware import Middleware


class PermissionMiddleware(Middleware):
    def before(self, request, response, *args):
        user = request.user()
        if not user:
            return response.redirect(name="login")
        if user.has_permission(args[0]):
            return request
        return response.redirect(name="dashboard")

    def after(self, request, response, *args):
        return request
