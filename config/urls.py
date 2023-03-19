from django.contrib import admin
from django.urls import path, include

# as views so names do not collide
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    # Allows us to go to the admin website
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    # built in login, class based views
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    # now the http://127.0.0.1:8000 is our home page
    path("", include("app.urls")),
]
