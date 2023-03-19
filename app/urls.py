from . import views
from django.urls import path

urlpatterns = [
    # empty path = homepage
    path("", views.home, name="app-home"),
    path("about/", views.about, name="app-about"),
]
