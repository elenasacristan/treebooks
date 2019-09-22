from django.conf.urls import url
from .views import edit_user_profile, view_profile

urlpatterns = [
    url(r'^$', view_profile, name='view_profile'),
    url(r'^edit/(?P<id>\d+)$', edit_user_profile, name='edit_user_profile'),
]
