from django.urls import path
from .views import add_remove_favourites

urlpatterns = [
    path('addremove/<int:id>/', add_remove_favourites, name='add_remove_favourites'),
]
