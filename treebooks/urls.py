from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_urls
from home import urls as home_urls
from userprofile import urls as profile_urls
from books import urls as books_urls
from cart import urls as cart_urls
from search import urls as search_urls
from checkout import urls as checkout_urls
from favourites import urls as favourites_urls
from reviews import urls as review_urls
from waiting_list import urls as waiting_list_urls
from home.views import index
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^home/', include(home_urls)),
    url(r'^profile/', include(profile_urls)),
    url(r'^books/', include(books_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^favourites/', include(favourites_urls)),
    url(r'^reviews/', include(review_urls)),
    url(r'^waiting_list/', include(waiting_list_urls)),
    url(r'media/(?P<path>.*)$', static.serve, {'document_root':MEDIA_ROOT}),
]
