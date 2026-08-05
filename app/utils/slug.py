"""Slug generation. Pure function, no DB access."""

import re

_MAX_LEN = 60
_DEFAULT = "workspace"


def slugify(name: str) -> str:
    """Return a URL-safe slug for the given name.

    Rules:
    1. Lowercase.
    2. Any non-alphanumeric run collapses to a single ``-``.
    3. Strip leading/trailing ``-``.
    4. Empty after step 3 → ``"workspace"``.
    5. Cap at 60 characters.
    """
    if not name:
        return _DEFAULT
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if not s:
        return _DEFAULT
    return s[:_MAX_LEN]
