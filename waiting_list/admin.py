from django.contrib import admin
from .models import WaitingList

# Register your models here.

# we add WaitingList model to the admin site
admin.site.register(WaitingList)


