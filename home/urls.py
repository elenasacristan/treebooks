from django.urls import path
from .views import index, about, donate, projects, contact

urlpatterns = [
    path('about/', about, name='about'),
    path('donate/', donate, name='donate'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]

