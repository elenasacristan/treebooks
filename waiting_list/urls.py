from django.conf.urls import url
from .views import join_waiting_list

urlpatterns = [
url (r'^(?P<pk>\d+)/$', join_waiting_list, name='join_waiting_list'),
]