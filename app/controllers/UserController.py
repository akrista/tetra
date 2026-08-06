"""Tenant-scoped user management (create, edit, delete)."""

from datetime import UTC, datetime

from masonite.controllers import Controller
from masonite.facades import Hash, Mail
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.controllers.AuthController import _auto_verify, _make_verify_hash
from app.mailables.VerifyEmailMailable import VerifyEmailMailable
from app.models.Role import Role
from app.models.User import User
from app.utils.auth_urls import verify_email_url


class UserController(Controller):
    def index(self, request: Request, view: View):
        user = request.user()
        users = User.where("tenant_id", user.tenant_id).order_by("name").get()
        return view.render(
            "app.users.index", {"users": users, "user": user, "active_page": "users"}
        )

    def create(self, request: Request, view: View):
        user = request.user()
        roles = Role.where("tenant_id", user.tenant_id).order_by("name").get()
        return view.render(
            "app.users.create",
            {"roles": roles, "user": user, "active_page": "users"},
        )

    def store(self, request: Request, response: Response):
        user = request.user()
        errors = request.validate(
            {
                "name": "required",
                "email": "required|email",
                "password": "required|confirmed",
            }
        )
        if not errors and len(request.input("password") or "") < 8:
            errors = {"password": ["La contraseña debe tener al menos 8 caracteres."]}
        if errors:
            return response.redirect("/users/create").with_errors(errors)

        email = request.input("email")
        if User.where("email", email).first():
            return response.redirect("/users/create").with_errors(
                {"email": "Ya existe una cuenta con este correo."}
            )

        auto = _auto_verify()
        new_user = User.create(
            {
                "tenant_id": user.tenant_id,
                "name": request.input("name"),
                "email": email,
                "phone": request.input("phone"),
                "password": Hash.make(request.input("password")),
                "verified_at": datetime.now(UTC).isoformat(sep=" ") if auto else None,
            }
        )

        role_id = request.input("role_id")
        role = self._assignable_role(user, role_id) if role_id else None
        if role:
            request.app.make("builder").new().table("role_user").create(
                {"user_id": new_user.id, "role_id": role.id}
            )

        if not auto:
            Mail.mailable(
                VerifyEmailMailable(
                    new_user.email,
                    new_user.name,
                    verify_email_url(new_user.id, _make_verify_hash(new_user)),
                )
            ).send()

        return response.redirect("/users").with_success("Usuario creado.")

    def edit(self, request: Request, response: Response, view: View):
        user = request.user()
        target = self._find(request)
        if not target:
            return response.redirect("/users")
        roles = self._assignable_roles(user)
        return view.render(
            "app.users.edit",
            {"target": target, "roles": roles, "user": user, "active_page": "users"},
        )

    def update(self, request: Request, response: Response):
        user = request.user()
        target = self._find(request)
        if not target:
            return response.redirect("/users")

        if target.is_owner and not user.is_owner:
            return response.redirect("/users").with_errors(
                {"delete": "Solo el dueño puede modificar una cuenta de dueño."}
            )

        errors = request.validate({"name": "required", "email": "required|email"})
        if errors:
            return response.redirect(f"/users/{target.id}/edit").with_errors(errors)

        email = request.input("email")
        if User.where("email", email).where("id", "!=", target.id).first():
            return response.redirect(f"/users/{target.id}/edit").with_errors(
                {"email": "Ya existe una cuenta con este correo."}
            )

        email_changed = email != target.email
        target.name = request.input("name")
        target.email = email
        target.phone = request.input("phone")
        if email_changed:
            target.verified_at = (
                datetime.now(UTC).isoformat(sep=" ") if _auto_verify() else None
            )
        target.save()

        builder = request.app.make("builder").new()
        builder.table("role_user").where("user_id", target.id).delete()
        role_id = request.input("role_id")
        role = self._assignable_role(user, role_id) if role_id else None
        if role:
            builder.table("role_user").create(
                {"user_id": target.id, "role_id": role.id}
            )

        if email_changed and not _auto_verify():
            Mail.mailable(
                VerifyEmailMailable(
                    target.email,
                    target.name,
                    verify_email_url(target.id, _make_verify_hash(target)),
                )
            ).send()

        return response.redirect("/users").with_success("Usuario actualizado.")

    def delete(self, request: Request, response: Response):
        user = request.user()
        target = self._find(request)
        if not target:
            return response.redirect("/users")

        if target.id == user.id:
            return response.redirect("/users").with_errors(
                {"delete": "No puedes eliminar tu propia cuenta."}
            )

        if target.is_owner and not user.is_owner:
            return response.redirect("/users").with_errors(
                {"delete": "Solo el dueño puede eliminar una cuenta de dueño."}
            )

        owners = User.where("tenant_id", user.tenant_id).where("is_owner", True).count()
        if target.is_owner and owners <= 1:
            return response.redirect("/users").with_errors(
                {"delete": "No puedes eliminar al último dueño."}
            )

        request.app.make("builder").new().table("role_user").where(
            "user_id", target.id
        ).delete()
        target.delete()
        return response.redirect("/users").with_success("Usuario eliminado.")

    def _find(self, request):
        try:
            user_id = int(request.param("id"))
        except (TypeError, ValueError):
            return None
        return (
            User.where("id", user_id)
            .where("tenant_id", request.user().tenant_id)
            .first()
        )

    def _assignable_roles(self, user):
        roles = Role.where("tenant_id", user.tenant_id).order_by("name").get()
        if user.is_owner:
            return roles
        held = user.permission_slugs()
        return [r for r in roles if set(r.permission_slugs()).issubset(held)]

    def _assignable_role(self, user, role_id):
        try:
            role_id = int(role_id)
        except (TypeError, ValueError):
            return None
        role = Role.where("id", role_id).where("tenant_id", user.tenant_id).first()
        if not role or user.is_owner:
            return role
        return (
            role
            if set(role.permission_slugs()).issubset(user.permission_slugs())
            else None
        )
