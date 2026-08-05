from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show").name("welcome"),
    # Authentication Routes
    Route.get("/login", "AuthController@show_login").name("login"),
    Route.post("/login", "AuthController@login"),
    Route.get("/register", "AuthController@show_register").name("register"),
    Route.post("/register", "AuthController@register"),
    Route.get("/password/forgot", "AuthController@show_forgot_password").name(
        "password.forgot"
    ),
    Route.post("/password/forgot", "AuthController@send_password_reset"),
    Route.get("/password/reset", "AuthController@show_reset_password").name(
        "password.reset"
    ),
    Route.post("/password/reset", "AuthController@reset_password"),
    Route.get("/verify-email", "AuthController@show_verify_email").name("verify.email"),
    Route.post("/logout", "AuthController@logout").name("logout"),
]
