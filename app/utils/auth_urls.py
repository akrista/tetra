"""URL builders for auth emails."""

from masonite.configuration import config


def app_url(path: str) -> str:
    base = str(config("application.APP_URL") or "http://localhost:8000").rstrip("/")
    return f"{base}{path}"


def password_reset_url(token: str) -> str:
    return app_url(f"/password/reset/{token}")


def verify_email_url(user_id: int, signed_hash: str) -> str:
    return app_url(f"/verify-email/{user_id}/{signed_hash}")
