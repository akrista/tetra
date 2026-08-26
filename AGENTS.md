<masonite-guidelines>
=== .ai/cognitive rules ===

## Developer Communication & Cognitive Ergonomics

As an AI assistant, your primary goal when explaining concepts, architectural decisions, code changes, or debugging
steps is to prevent **Cognitive Overload** for the developer. You MUST adhere to the following cognitive ergonomics
rules:

### 1. Strict Quantitative Limits (Chunking)

- **No walls of text.** Limit explanations of complex logic, architectural patterns, or bug analysis to a maximum of
150-200 words.
- **Actionable brevity:** Focus ONLY on what the developer needs to know right now to make a decision or understand the
code. Drop unnecessary historical context or overly verbose pleasantries.

### 2. Progressive Disclosure

- If an explanation requires more depth than the allowed limit, you MUST use progressive disclosure.
- Provide a high-level summary (maximum 3 bullet points) and then **stop**. Explicitly ask the user which specific point
they would like to explore further before generating more text.

### 3. Extraneous Load Reduction (Formatting)

- **Visual Hierarchy:** Use clear headings (`###`) and bulleted lists to structure your responses.
- **Scannability:** Always **bold** key terminology, class names, method names, and file paths so the developer's eyes
can scan them instantly.
- Keep paragraphs to a maximum of 3 lines.

### 4. Anchoring via Analogies

- When introducing a new or highly complex Masonite/Python concept (e.g., the Service Container, Provider boot order,
or async queue jobs), anchor the technical explanation with a simple, real-world analogy (e.g., cooking,
manufacturing, logistics) in exactly one sentence.

### 5. Code Presentation

- State exactly what the code does in 1 to 2 sentences max.
- Output the code block.
- Do not add massive blocks of explanatory text *after* the code unless strictly necessary. Let the code (and its
docstrings) speak for itself. Wait for the developer to ask for clarification.

=== foundation rules ===

# Masonite Guidelines

The Masonite guidelines are specifically curated for this application. These guidelines should be followed closely to ensure the best experience when building Masonite applications.

## Foundational Context

This application is a Masonite application built on the following ecosystem packages & versions. You are an expert with them all. Ensure you abide by these specific packages & versions.

- python - 3.12+
- masonite-framework (MASONITE) - v5
- masonite-framework-orm (MASONITEORM) - v3
- tigerbeetle (TIGERBETTLE) - v0.17
- pytest (PYTEST) - v9
- ruff (RUFF) - v0.16
- pre-commit (PRECOMMIT) - v4.6
- uv (UV) - dependency & venv management
- vite (VITE) - v8
- tailwindcss (TAILWINDCSS) - v4
- bun (BUN) - frontend tooling

## Skills Activation

This project has domain-specific skills available in `**/skills/**`. You MUST activate the relevant skill whenever you work in that domain—don't wait until you're stuck.

## Conventions

- You must follow all existing code conventions used in this application. When creating or editing a file, check sibling files for the correct structure, approach, and naming.
- Use descriptive names for variables and methods. For example, `is_registered_for_discounts`, not `discount()`.
- Check for existing components to reuse before writing a new one.

## Verification Scripts

- Do not create verification scripts or scratch test files when tests cover that functionality and prove they work. Tests are more important.

## Application Structure & Architecture

- Stick to existing directory structure; don't create new base folders without approval.
- Do not change the application's dependencies without approval.

## Frontend Bundling

- If the user doesn't see a frontend change reflected in the UI, it could mean they need to run `bun run dev` or `bun run prod`. Ask them.

## Documentation Files

- You must only create documentation files if explicitly requested by the user.

## Replies

- Be concise in your explanations - focus on what's important rather than explaining obvious details.

=== craft rules ===

# Craft Command Line

- Masonite's CLI is `craft`. Run commands via `python craft <command>` (e.g., `python craft route:list`). Use `python craft` to discover available commands and `python craft <command> --help` to check parameters.
- Inspect routes with `python craft route:list`. Filter with `--method=GET`, `--name=users`, `--path=api`.
- Read configuration values from `config/` files directly (e.g., `config/application.py`, `config/database.py`).

## Database

- Run migrations with `python craft migrate` and rollbacks with `python craft migrate:rollback`.
- Inspect the database with read-only queries; prefer the ORM (`Model.where(...)`) over raw SQL.

=== python rules ===

# Python

- Use snake_case for functions, methods, and variables: `is_registered_for_discounts`, not `discount()`.
- Use explicit return type annotations and type hints for all method parameters: `def is_accessible(user: User, path: str | None = None) -> bool`.
- Use `str | None` over `Optional[str]`.
- Use `ClassVar[list[str]]` type annotations for MasoniteORM magic attributes like `__fillable__` and `__hidden__`.
- Prefer module-level docstrings and concise method docstrings over inline comments. Only add inline comments for exceptionally complex logic.
- Use Python's `@dataclass` or plain classes; don't introduce single-use abstractions.

=== tests rules ===

# Test Enforcement

- Every change must be programmatically tested. Write a new test or update an existing test, then run the affected tests to make sure they pass.
- This project uses **pytest** with **class-based test cases** extending `tests/TestCase.py` (which extends `masonite.tests.TestCase`). Follow the existing style in `tests/`.
- Run the minimum number of tests needed to ensure code quality and speed: `python -m pytest tests/test_file.py -x -q` or filter with `-k test_name`.
- Reuse the helpers on `TestCase`: `make_tenant()`, `make_user()`, `make_role()`, `login_as()`.
- Do NOT delete tests without approval.

=== masonite/core rules ===

# Do Things the Masonite Way

- Prefer existing Masonite conventions and the Service Container over custom globals or singletons.
- Register application service providers in `config/providers.py` and custom app providers under `app/providers/`.
- Use `craft` commands to scaffold where available. Pass the correct `--options` to ensure correct behavior.

### Models

- Models live in `app/models/` and extend `masoniteorm.models.Model`. Use MasoniteORM magic attributes (`__table__`, `__fillable__`, `__hidden__`) and relationship decorators (`@belongs_to`, `@has_many`, `@belongs_to_many`).
- This app is **tenant-scoped**: models carry a `tenant_id` and queries must filter by it. Do not write cross-tenant queries.
- Use `from app.models.X import X` absolute imports, matching existing model files.

### Controllers

- Controllers live in `app/controllers/` and extend `masonite.controllers.Controller`. Inject dependencies (e.g., `Request`, `View`, services) via constructor or method injection from the container.
- Route string format is `"ControllerName@method"`.

### Routes

- Web routes go in `routes/web.py`, API routes in `routes/api.py`. Use `Route.get(path, controller)`, `.name(...)`, `.middleware(...)` chains as shown in `routes/web.py`.
- Route parameters use `@` (e.g., `/users/@id/edit`). Named routes are preferred for URL generation.
- Authenticated or permission-gated routes must apply the `"auth"` and `"permission:slug"` middlewares.

### Middleware

- Middlewares live in `app/middlewares/` and implement `before(request, response, ...)`. Register them in `config/middleware.py` and attach via `Route.middleware("name")`.

### Auth & RBAC

- User auth uses the `Authenticates` mixin and `Notifiable` mixin from Masonite (`app/models/User.py`).
- RBAC is role/permission based with tenant scoping. Use the `can(slug)` helper on `User` and the `permission:slug` route middleware (`app/middlewares/PermissionMiddleware.py`). Owner users bypass permission checks.

### Templates

- Views are rendered with `View` via `view.render("app.dashboard", {...})` and live in `templates/`. Use named route helpers in templates (e.g., `route('users')`).

## URL Generation

- When generating links to other pages, prefer named routes via the `route()` helper.

## Testing

- Extend `tests/TestCase.py` rather than raw `masonite.tests.TestCase` so you get the tenant/user/role factories and per-test table wipe.
- Assert HTTP responses with the test client chain, e.g. `self.get("/").assertOk().assertContains("Tetra")`.

## Vite Error

- If you receive a Vite manifest error (missing built assets), run `bun run dev` or `bun run prod`.

=== lint/format rules ===

# Ruff & Pre-commit

- This project uses **ruff** for linting and formatting (config in `pyproject.toml`, hooks in `.pre-commit-config.yaml`).
- If you have modified any Python files, run `uv run ruff check --fix .` and `uv run ruff format .` before finalizing changes.
- The pre-commit config runs `ruff-check --fix` and `ruff-format`; you can run `uv run pre-commit run --all-files` to verify.
- Do not add inline `# noqa` comments unless a rule genuinely cannot be satisfied.

=== deployments rules ===

# Deployment

- Masonite WSGI apps are deployed as any Python WSGI application via the `wsgi.py` entry point. Use the project's existing deployment approach; don't invent new infrastructure without approval.

=== dev server rules ===

# Dev Server

- The application is served locally with `python craft serve` (defaults to `http://localhost:8000`). Never run commands that fight the running dev server; it is already available.
- Use `APP_URL` from `config/application.py` / `.env` to generate valid URLs.

</masonite-guidelines>
