import platform

from masonite import __version__ as masonite_version
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
                "version": masonite_version,
                "python_version": platform.python_version(),
                "request": request,
                "user": Auth.user(),
            },
        )
