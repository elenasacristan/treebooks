from django.urls import path
from .views import edit_user_profile, view_profile

urlpatterns = [
    path('', view_profile, name='view_profile'),
    path('edit/<int:id>/', edit_user_profile, name='edit_user_profile'),
]
