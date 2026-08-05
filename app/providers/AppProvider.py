from masonite.providers import Provider
from masonite.request import Request


class AppProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        pass

    def boot(self):
        Request.tenant = lambda self: getattr(self, "_tenant", None)
