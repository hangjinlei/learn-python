from django.urls import path
from . import views

urlpatterns = [
    path("playground/hello/<name>", views.sya_hello, name="hello")
]
