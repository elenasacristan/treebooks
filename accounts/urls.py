from django.urls import path, include
from .views import login, logout, registration
from accounts import url_reset


urlpatterns = [
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('password-reset/', include(url_reset)),
]

