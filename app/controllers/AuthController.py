"""Auth flows: register, login, logout, password reset, email verification."""

from datetime import UTC, datetime

from masonite.auth import Sign
from masonite.authentication import Auth
from masonite.controllers import Controller
from masonite.environment import env
from masonite.facades import Hash, Mail
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.mailables.PasswordResetMailable import PasswordResetMailable
from app.mailables.VerifyEmailMailable import VerifyEmailMailable
from app.models.Tenant import Tenant
from app.models.User import User
from app.utils.auth_urls import password_reset_url, verify_email_url
from app.utils.slug import slugify


def _auto_verify() -> bool:
    return env("MAIL_DRIVER", "terminal") == "terminal"


def _make_verify_hash(user) -> str:
    return Sign().sign(f"{user.id}::{user.email}")


def _allocate_slug(name: str) -> str:
    base = slugify(name)
    slug = base
    i = 2
    while Tenant.where("slug", slug).first():
        slug = f"{base}-{i}"
        i += 1
        if i > 50:
            raise RuntimeError("Could not allocate tenant slug")
    return slug


class AuthController(Controller):
    def show_login(self, request: Request, view: View):
        if request.user():
            return request.redirect("/")
        return view.render("auth.login")

    def login(self, request: Request, auth: Auth, response: Response):
        errors = request.validate(
            {
                "email": "required|email",
                "password": "required",
            }
        )
        if errors:
            return response.redirect("/login").with_errors(errors)

        if not auth.attempt(request.input("email"), request.input("password")):
            return response.redirect("/login").with_errors(
                {"login": "Invalid email or password."}
            )

        user = request.user()
        request.session.set("tenant_id", user.tenant_id)
        return response.redirect("/")

    def show_register(self, request: Request, view: View):
        if request.user():
            return request.redirect("/")
        return view.render("auth.register")

    def register(self, request: Request, auth: Auth, response: Response):
        errors = request.validate(
            {
                "name": "required",
                "email": "required|email",
                "password": "required|confirmed",
                "tenant_name": "required",
            }
        )
        if not errors:
            pw = request.input("password") or ""
            if len(pw) < 8:
                errors = {"password": ["Password must be at least 8 characters."]}
        if errors:
            return response.redirect("/register").with_errors(errors)

        email = request.input("email")
        if User.where("email", email).first():
            return response.redirect("/register").with_errors(
                {"email": "An account with this email already exists."}
            )

        auto = _auto_verify()
        tenant = Tenant.create(
            {
                "name": request.input("tenant_name"),
                "slug": _allocate_slug(request.input("tenant_name")),
            }
        )
        user = User.create(
            {
                "name": request.input("name"),
                "email": email,
                "password": Hash.make(request.input("password")),
                "tenant_id": tenant.id,
                "is_owner": True,
                "verified_at": datetime.now(UTC).isoformat(sep=" ") if auto else None,
            }
        )

        auth.attempt_by_id(user.id)
        request.session.set("tenant_id", user.tenant_id)

        if not auto:
            Mail.mailable(
                VerifyEmailMailable(
                    user.email,
                    user.name,
                    verify_email_url(user.id, _make_verify_hash(user)),
                )
            ).send()
            return response.redirect("/verify-email")

        return response.redirect("/")

    def logout(self, request: Request, auth: Auth, response: Response):
        auth.logout()
        request.session.flush()
        return response.redirect("/login")

    def show_forgot_password(self, view: View):
        return view.render("auth.forgot_password")

    def send_password_reset(self, request: Request, auth: Auth, response: Response):
        errors = request.validate({"email": "required|email"})
        if errors:
            return response.redirect("/password/forgot").with_errors(errors)

        email = request.input("email")
        result = auth.password_reset(email)
        _, token = (None, None)
        if result:
            _, token = result
        if token:
            user = User.where("email", email).first()
            if user:
                Mail.mailable(
                    PasswordResetMailable(
                        user.email, user.name, password_reset_url(token)
                    )
                ).send()

        return response.redirect("/password/forgot").with_success(
            "If an account exists for that email, we sent a reset link."
        )

    def show_reset_password(self, request: Request, view: View):
        token = request.param("token") or ""
        email = request.input("email", "")

        is_valid = False
        resolved_email = email
        if token:
            row = (
                request.app.make("builder")
                .new()
                .table("password_resets")
                .where("token", token)
                .first()
            )
            if row:
                expires_at = row.get("expires_at")
                expired = True
                if expires_at:
                    try:
                        exp_dt = datetime.fromisoformat(str(expires_at))
                    except ValueError:
                        exp_dt = None
                    if exp_dt and exp_dt >= datetime.now(UTC).replace(tzinfo=None):
                        expired = False
                if not expired:
                    is_valid = True
                    if not resolved_email:
                        resolved_email = row.get("email", "")

        return view.render(
            "auth.reset_password",
            {"token": token, "email": resolved_email, "is_valid": is_valid},
        )

    def reset_password(self, request: Request, auth: Auth, response: Response):
        token = request.input("token", "")
        errors = request.validate(
            {
                "email": "required|email",
                "password": "required|confirmed",
            }
        )
        if not errors and len(request.input("password") or "") < 8:
            errors = {"password": ["Password must be at least 8 characters."]}
        if errors:
            return (
                response.redirect(f"/password/reset/{token}")
                .with_errors(errors)
                .with_input(request.all())
            )

        if not auth.reset_password(request.input("password"), token):
            return response.redirect(f"/password/reset/{token}").with_errors(
                {"reset": "Invalid or expired link."}
            )

        return response.redirect("/login").with_success(
            "Password updated. Please sign in."
        )

    def show_verify_email(self, request: Request, view: View):
        return view.render("auth.verify_email")

    def verify_email(self, request: Request, response: Response):
        user = request.user()
        if not user:
            return response.redirect("/login")

        try:
            user_id = int(request.param("id"))
        except TypeError, ValueError:
            return response.redirect("/verify-email").with_errors(
                {"verify": "Invalid verification link."}
            )

        if user.id != user_id:
            return response.redirect("/verify-email").with_errors(
                {"verify": "Link is for a different account."}
            )

        expected = _make_verify_hash(user)
        if request.param("hash") != expected:
            return response.redirect("/verify-email").with_errors(
                {"verify": "Invalid verification link."}
            )

        if user.verified_at:
            return response.redirect("/").with_success("Email already verified.")

        User.where("id", user.id).update(
            {"verified_at": datetime.now(UTC).isoformat(sep=" ")}
        )
        return response.redirect("/").with_success("Email verified.")

    def resend_verify_email(self, request: Request, response: Response):
        user = request.user()
        if not user:
            return response.redirect("/login")

        Mail.mailable(
            VerifyEmailMailable(
                user.email,
                user.name,
                verify_email_url(user.id, _make_verify_hash(user)),
            )
        ).send()

        return response.redirect("/verify-email").with_success(
            "Verification email resent."
        )
