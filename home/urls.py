from django.conf.urls import url
from .views import index, about, donate, projects, contact


urlpatterns = [
    url(r'^about/$', about, name='about'),
    url(r'^donate/$', donate, name='donate'),
    url(r'^projects/$', projects, name='projects'),
    url(r'^contact/$', contact, name='contact'),

]

