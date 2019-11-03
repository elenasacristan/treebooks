from django.contrib import admin
from .models import UserProfile

# Register your models here.

# we add UserProfile model to the admin site
admin.site.register(UserProfile)