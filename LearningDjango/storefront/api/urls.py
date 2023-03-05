from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("items/", views.items),
    path("items/<int:pk>/", views.item),
    path("items-view/<int:pk>/", views.ItemsView.as_view()),
    path("items-view-mix/", views.ItemsViewMix.as_view()),
    path("item-generics-list/", views.ItemList.as_view()),
    path("item-generics-detail/", views.ItemDetail.as_view()),
]

# http://127.0.0.1:3000/api/items/1.json/?format=json
urlpatterns = format_suffix_patterns(urlpatterns)
