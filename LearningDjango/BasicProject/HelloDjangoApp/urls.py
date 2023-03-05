## App

from django.urls import path, re_path
from . import views

urlpatterns = [
    path(route=r"", view=views.index, name="index"),
    re_path(route=r"home$", view=views.index, name="home"),
    re_path(route=r"^about$", view=views.about, name="about"),
]
