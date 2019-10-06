from django.conf.urls import url
from .views import add_review

urlpatterns = [
# url (r'^(?P<pk>\d+)/$', add_review, name='add_review'),
url (r'^$', add_review, name='add_review'),

]