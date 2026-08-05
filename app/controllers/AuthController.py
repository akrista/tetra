from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View


class AuthController(Controller):
    def show_login(self, view: View):
        return view.render("auth.login")

    def login(self, request: Request, response: Response):
        email = request.input("email")
        password = request.input("password")
        if not email or not password:
            return response.redirect("/login").with_errors(
                {"login": "Invalid email or password."}
            )
        return response.redirect("/")

    def show_register(self, view: View):
        return view.render("auth.register")

    def register(self, request: Request, response: Response):
        name = request.input("name")
        email = request.input("email")
        password = request.input("password")
        if not name or not email or not password:
            return response.redirect("/register").with_errors(
                {"register": "All fields are required."}
            )
        return response.redirect("/login")

    def show_forgot_password(self, view: View):
        return view.render("auth.forgot_password")

    def send_password_reset(self, request: Request, response: Response):
        email = request.input("email")
        if not email:
            return response.redirect("/password/forgot").with_errors(
                {"email": "Email is required."}
            )
        return response.redirect("/password/forgot").with_success(
            "Password reset link sent to your email."
        )

    def show_reset_password(self, request: Request, view: View):
        token = request.param("token", "")
        email = request.input("email", "")
        return view.render("auth.reset_password", {"token": token, "email": email})

    def reset_password(self, request: Request, response: Response):
        password = request.input("password")
        if not password:
            return response.redirect("/password/reset").with_errors(
                {"password": "Password is required."}
            )
        return response.redirect("/login")

    def show_verify_email(self, view: View):
        return view.render("auth.verify_email")

    def logout(self, response: Response):
        return response.redirect("/login")
