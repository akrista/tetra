"""URL builders for auth emails."""

from masonite.configuration import config


def password_reset_url(token: str) -> str:
    base = str(config("application.APP_URL") or "http://localhost:8000").rstrip("/")
    return f"{base}/password/reset/{token}"


def verify_email_url(user_id: int, signed_hash: str) -> str:
    base = str(config("application.APP_URL") or "http://localhost:8000").rstrip("/")
    return f"{base}/verify-email/{user_id}/{signed_hash}"
