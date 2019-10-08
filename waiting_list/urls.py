from django.conf.urls import url
from .views import join_waiting_list, view_waiting_lists

urlpatterns = [
url (r'^(?P<pk>\d+)/$', view_waiting_lists, name='view_waiting_lists'),
url (r'^join/(?P<pk>\d+)/$', join_waiting_list, name='join_waiting_list'),
]