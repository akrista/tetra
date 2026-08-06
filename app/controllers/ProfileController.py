"""Profile: edit own data, change password, change email."""

from datetime import UTC, datetime

from masonite.controllers import Controller
from masonite.facades import Hash, Mail
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.controllers.AuthController import _auto_verify, _make_verify_hash
from app.mailables.VerifyEmailMailable import VerifyEmailMailable
from app.models.User import User
from app.utils.auth_urls import verify_email_url


class ProfileController(Controller):
    def show(self, request: Request, view: View):
        user = request.user()
        return view.render(
            "app.profile",
            {"user": user, "tenant": user.tenant, "active_page": "profile"},
        )

    def update(self, request: Request, response: Response):
        user = request.user()
        errors = request.validate({"name": "required"})
        if errors:
            return response.redirect("/profile").with_errors(errors)

        user.name = request.input("name")
        user.phone = request.input("phone")
        user.save()
        return response.redirect("/profile").with_success("Datos actualizados.")

    def password(self, request: Request, response: Response):
        user = request.user()
        errors = request.validate(
            {
                "current_password": "required",
                "password": "required|confirmed",
            }
        )
        if not errors and len(request.input("password") or "") < 8:
            errors = {"password": ["La contraseña debe tener al menos 8 caracteres."]}
        if errors:
            return response.redirect("/profile").with_errors(errors)

        if not Hash.check(request.input("current_password"), user.password):
            return response.redirect("/profile").with_errors(
                {"current_password": "La contraseña actual no es correcta."}
            )

        user.password = Hash.make(request.input("password"))
        user.set_remember_token().save()
        response.cookie("token", user.remember_token)
        return response.redirect("/profile").with_success("Contraseña actualizada.")

    def email(self, request: Request, response: Response):
        user = request.user()
        errors = request.validate(
            {
                "email": "required|email",
                "current_password": "required",
            }
        )
        if errors:
            return response.redirect("/profile").with_errors(errors)

        if not Hash.check(request.input("current_password"), user.password):
            return response.redirect("/profile").with_errors(
                {"current_password": "La contraseña actual no es correcta."}
            )

        new_email = request.input("email")
        if new_email == user.email:
            return response.redirect("/profile").with_success("El correo no cambió.")

        if User.where("email", new_email).where("id", "!=", user.id).first():
            return response.redirect("/profile").with_errors(
                {"email": "Ya existe una cuenta con este correo."}
            )

        user.email = new_email
        if _auto_verify():
            user.verified_at = datetime.now(UTC).isoformat(sep=" ")
        else:
            user.verified_at = None
            Mail.mailable(
                VerifyEmailMailable(
                    user.email,
                    user.name,
                    verify_email_url(user.id, _make_verify_hash(user)),
                )
            ).send()
        user.save()
        return response.redirect("/profile").with_success(
            "Correo actualizado. Revisa tu bandeja para verificar."
        )
