from django.conf.urls import url, include
from .views import login, logout, registration
from accounts import url_reset


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^password-reset/', include(url_reset)),
]

