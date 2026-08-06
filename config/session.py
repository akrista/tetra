from masonite.environment import env


def _cookie_secure() -> bool:
    value = env("COOKIE_SECURE", "false")
    if isinstance(value, bool):
        return value
    return str(value).lower() in ("1", "true", "yes", "on")


DRIVERS = {
    "default": "cookie",
    "cookie": {"secure": _cookie_secure()},
    "redis": {
        "host": "127.0.0.1",
        "port": 6379,
        "password": "",
        "options": {"db": 1},  # redis module driver specific options
        "timeout": 60 * 60,
        "namespace": "masonite",
    },
}
