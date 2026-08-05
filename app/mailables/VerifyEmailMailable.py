"""Email verification link."""

from masonite.mail import Mailable


class VerifyEmailMailable(Mailable):
    def __init__(self, to_email: str, name: str, verify_url: str):
        super().__init__()
        self._to = to_email
        self._subject = "Verify your email"
        self._name = name
        self._verify_url = verify_url

    def build(self):
        return (
            self.subject(self._subject)
            .to(self._to)
            .view(
                "emails.verify_email",
                {"name": self._name, "verify_url": self._verify_url},
            )
        )
