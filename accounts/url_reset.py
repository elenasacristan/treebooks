from django.urls import path, reverse_lazy

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

"""
These are the urls needed for the reset password functionality
and they will be imported into the urls.py (accounts app)
"""
urlpatterns = [
    path('', PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]