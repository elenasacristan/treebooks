from django.conf.urls import url
from .views import view_all_books, detail


urlpatterns = [
    url(r'^$', view_all_books, name='view_all_books'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),

]

