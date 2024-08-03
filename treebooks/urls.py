from django.urls import path, include
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
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include(accounts_urls)),
    path('home/', include(home_urls)),
    path('profile/', include(profile_urls)),
    path('books/', include(books_urls)),
    path('cart/', include(cart_urls)),
    path('search/', include(search_urls)),
    path('checkout/', include(checkout_urls)),
    path('favourites/', include(favourites_urls)),
    path('reviews/', include(review_urls)),
    path('waiting_list/', include(waiting_list_urls)),
    path('media/<path:path>/', static.serve, {'document_root': MEDIA_ROOT}),
]
