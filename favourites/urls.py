from django.conf.urls import url
from .views import add_remove_favourites

urlpatterns = [
    url(r'^addremove/(?P<id>\d+)$', add_remove_favourites, name='add_remove_favourites'),
]
