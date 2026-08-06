"""Tenant-scoped role & permission management."""

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Permission import Permission
from app.models.Role import Role
from app.utils.slug import slugify


class RoleController(Controller):
    def index(self, request: Request, view: View):
        user = request.user()
        roles = Role.where("tenant_id", user.tenant_id).order_by("name").get()
        builder = request.app.make("builder").new()
        role_data = []
        for role in roles:
            role_data.append(
                {
                    "role": role,
                    "permissions": [p.name for p in role.permissions],
                    "user_count": builder.table("role_user")
                    .where("role_id", role.id)
                    .count(),
                }
            )
        return view.render(
            "app.roles.index",
            {"role_data": role_data, "user": user, "active_page": "roles"},
        )

    def create(self, request: Request, view: View):
        user = request.user()
        return view.render(
            "app.roles.create",
            {
                "permissions": self._grantable_permissions(user),
                "user": user,
                "active_page": "roles",
            },
        )

    def store(self, request: Request, response: Response):
        user = request.user()
        errors = request.validate({"name": "required"})
        if errors:
            return response.redirect("/roles/create").with_errors(errors)

        name = request.input("name")
        slug = slugify(name)
        if Role.where("tenant_id", user.tenant_id).where("slug", slug).first():
            return response.redirect("/roles/create").with_errors(
                {"name": "Ya existe un rol con este nombre."}
            )

        role = Role.create({"tenant_id": user.tenant_id, "name": name, "slug": slug})
        self._sync_permissions(request, user, role)
        return response.redirect("/roles").with_success("Rol creado.")

    def edit(self, request: Request, response: Response, view: View):
        user = request.user()
        role = self._find(request)
        if not role:
            return response.redirect("/roles")
        return view.render(
            "app.roles.edit",
            {
                "target": role,
                "permissions": self._grantable_permissions(user),
                "checked": role.permission_slugs(),
                "user": user,
                "active_page": "roles",
            },
        )

    def update(self, request: Request, response: Response):
        user = request.user()
        role = self._find(request)
        if not role:
            return response.redirect("/roles")

        errors = request.validate({"name": "required"})
        if errors:
            return response.redirect(f"/roles/{role.id}/edit").with_errors(errors)

        name = request.input("name")
        slug = slugify(name)
        dup = (
            Role.where("tenant_id", user.tenant_id)
            .where("slug", slug)
            .where("id", "!=", role.id)
            .first()
        )
        if dup:
            return response.redirect(f"/roles/{role.id}/edit").with_errors(
                {"name": "Ya existe un rol con este nombre."}
            )

        if not user.is_owner and not set(role.permission_slugs()).issubset(
            user.permission_slugs()
        ):
            return response.redirect(f"/roles/{role.id}/edit").with_errors(
                {
                    "delete": "No puedes editar este rol: contiene permisos que no posees."
                }
            )

        role.name = name
        role.slug = slug
        role.save()
        self._sync_permissions(request, user, role)
        return response.redirect("/roles").with_success("Rol actualizado.")

    def delete(self, request: Request, response: Response):
        role = self._find(request)
        if not role:
            return response.redirect("/roles")

        count = (
            request.app.make("builder")
            .new()
            .table("role_user")
            .where("role_id", role.id)
            .count()
        )
        if count > 0:
            return response.redirect("/roles").with_errors(
                {"delete": f"No se puede eliminar: {count} usuario(s) tienen este rol."}
            )
        role.delete()
        return response.redirect("/roles").with_success("Rol eliminado.")

    def _find(self, request):
        try:
            role_id = int(request.param("id"))
        except (TypeError, ValueError):
            return None
        return (
            Role.where("id", role_id)
            .where("tenant_id", request.user().tenant_id)
            .first()
        )

    def _grantable_permissions(self, user):
        perms = Permission.order_by("slug").get()
        if user.is_owner and not perms:
            from types import SimpleNamespace

            from app.utils.rbac import PERMISSIONS

            return [SimpleNamespace(slug=slug, name=name) for slug, name in PERMISSIONS]
        return [p for p in perms if user.is_owner or user.can(p.slug)]

    def _sync_permissions(self, request, user, role):
        builder = request.app.make("builder").new()
        builder.table("permission_role").where("role_id", role.id).delete()
        selected = request.input("permissions", [])
        if isinstance(selected, str):
            selected = [selected]
        for slug in selected:
            if not slug or not (user.is_owner or user.can(slug)):
                continue
            perm = Permission.where("slug", slug).first()
            if not perm:
                perm = Permission.create({"slug": slug, "name": slug})
            builder.table("permission_role").create(
                {"role_id": role.id, "permission_id": perm.id}
            )
