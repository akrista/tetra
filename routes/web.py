from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show").name("welcome"),
    Route.get("/login", "AuthController@show_login").name("login"),
    Route.post("/login", "AuthController@login"),
    Route.get("/register", "AuthController@show_register").name("register"),
    Route.post("/register", "AuthController@register"),
    Route.post("/logout", "AuthController@logout").name("logout"),
    Route.get("/password/forgot", "AuthController@show_forgot_password").name(
        "password.forgot"
    ),
    Route.post("/password/forgot", "AuthController@send_password_reset"),
    Route.get("/password/reset/@token", "AuthController@show_reset_password").name(
        "password.reset"
    ),
    Route.post("/password/reset", "AuthController@reset_password"),
    Route.get("/verify-email", "AuthController@show_verify_email").name("verify.email"),
    Route.get("/verify-email/@id/@hash:any", "AuthController@verify_email"),
    Route.post("/verify-email/resend", "AuthController@resend_verify_email")
    .name("verify.resend")
    .middleware("auth"),
    Route.get("/dashboard", "DashboardController@show")
    .name("dashboard")
    .middleware("auth"),
    Route.get("/profile", "ProfileController@show").name("profile").middleware("auth"),
    Route.post("/profile", "ProfileController@update").middleware("auth"),
    Route.post("/profile/password", "ProfileController@password").middleware("auth"),
    Route.post("/profile/email", "ProfileController@email").middleware("auth"),
    Route.get("/users", "UserController@index")
    .name("users")
    .middleware("auth", "permission:users.manage"),
    Route.get("/users/create", "UserController@create")
    .name("users.create")
    .middleware("auth", "permission:users.manage"),
    Route.post("/users", "UserController@store")
    .name("users.store")
    .middleware("auth", "permission:users.manage"),
    Route.get("/users/@id/edit", "UserController@edit")
    .name("users.edit")
    .middleware("auth", "permission:users.manage"),
    Route.post("/users/@id", "UserController@update")
    .name("users.update")
    .middleware("auth", "permission:users.manage"),
    Route.post("/users/@id/delete", "UserController@delete")
    .name("users.delete")
    .middleware("auth", "permission:users.manage"),
    Route.get("/roles", "RoleController@index")
    .name("roles")
    .middleware("auth", "permission:roles.manage"),
    Route.get("/roles/create", "RoleController@create")
    .name("roles.create")
    .middleware("auth", "permission:roles.manage"),
    Route.post("/roles", "RoleController@store")
    .name("roles.store")
    .middleware("auth", "permission:roles.manage"),
    Route.get("/roles/@id/edit", "RoleController@edit")
    .name("roles.edit")
    .middleware("auth", "permission:roles.manage"),
    Route.post("/roles/@id", "RoleController@update")
    .name("roles.update")
    .middleware("auth", "permission:roles.manage"),
    Route.post("/roles/@id/delete", "RoleController@delete")
    .name("roles.delete")
    .middleware("auth", "permission:roles.manage"),
]
