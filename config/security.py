"""Security Related Config"""

from masonite.environment import env

# Cross-Origin Resource Sharing
# ponytail: restrict to localhost for dev; set CORS_ORIGINS env var in production.
CORS_ORIGINS = env("CORS_ORIGINS", "http://localhost:8000,http://127.0.0.1:8000")
CORS = {
    "paths": ["api/*"],
    "allowed_methods": ["*"],
    "allowed_origins": CORS_ORIGINS.split(",") if CORS_ORIGINS else [],
    "allowed_headers": ["*"],
    "exposed_headers": [],
    "max_age": None,
    "supports_credentials": False,
}
