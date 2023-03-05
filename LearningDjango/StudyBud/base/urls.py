from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route='room/<str:pk>/', view=views.room, name="room"),
    path(route="create-room/", view=views.createRoom, name="create-room"),
    path(route="update-room/<str:pk>/",
         view=views.updateRoom, name="update-room"),
    path(route="delete-room/<str:pk>/",
         view=views.deleteRoom, name="delete-room"),
]
