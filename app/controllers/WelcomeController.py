from masonite.controllers import Controller
from masonite.facades import Auth
from masonite.request import Request
from masonite.response import Response
from masonite.views import View


class WelcomeController(Controller):
    def show(self, view: View, request: Request, response: Response):
        if request.user():
            return response.redirect("/dashboard")
        return view.render(
            "welcome",
            {
                "request": request,
                "user": Auth.user(),
            },
        )
