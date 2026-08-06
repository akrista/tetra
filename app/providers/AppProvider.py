from masonite.facades import RateLimiter
from masonite.providers import Provider
from masonite.rates.limiters import GuestsOnlyLimiter


class AppProvider(Provider):
    def boot(self):
        for name in ("login", "register", "forgot", "reset", "resend"):
            RateLimiter.register(name, GuestsOnlyLimiter("5/minute"))
