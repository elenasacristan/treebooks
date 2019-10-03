from django.conf.urls import url
from .views import add_remove_favourites, see_favourites

urlpatterns = [
    # url(r'^add/$', add_to_favourites, name='add_to_favourites'),
    url(r'^$', see_favourites, name='see_favourites'),
    url(r'^addremove/(?P<id>\d+)$', add_remove_favourites, name='add_remove_favourites'),
]
