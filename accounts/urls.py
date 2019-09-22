from django.conf.urls import url, include
from .views import login, logout, registration
from accounts import url_reset
# from .models import Profile


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registration/$', registration, name='registration'),
    # url(r'^profile/$', user_profile, name='profile'),
    url(r'^password-reset/', include(url_reset)),
    # url(r'^profile/edit/(?P<id>\d+)$', edit, name='edit'),
]

