from django.contrib import admin
from .models import ContactUs, Projects, TotalRaised


# Register your models here.
# we add ContactUS, Projects and TotalRaised models to the admin site

admin.site.register(ContactUs)

admin.site.register(Projects)

admin.site.register(TotalRaised)

