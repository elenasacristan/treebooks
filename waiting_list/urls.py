from django.urls import path
from .views import join_waiting_list, view_waiting_lists

urlpatterns = [
    path('<int:pk>/', view_waiting_lists, name='view_waiting_lists'),
    path('join/<int:pk>/', join_waiting_list, name='join_waiting_list'),
]
