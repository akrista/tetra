"""Password reset email."""

from masonite.mail import Mailable


class PasswordResetMailable(Mailable):
    def __init__(self, to_email: str, name: str, reset_url: str):
        super().__init__()
        self._to = to_email
        self._subject = "Reset your password"
        self._name = name
        self._reset_url = reset_url

    def build(self):
        return (
            self.subject(self._subject)
            .to(self._to)
            .view(
                "emails.password_reset",
                {"name": self._name, "reset_url": self._reset_url},
            )
        )
