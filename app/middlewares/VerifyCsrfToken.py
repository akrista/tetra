from typing import ClassVar

from masonite.middleware import VerifyCsrfToken as Middleware


class VerifyCsrfToken(Middleware):
    exempt: ClassVar[list[str]] = []
