from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
'''
TabularInline subclass defines the template used to render the
order in the admin interface. StackedInline is another option
'''
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

'''
The admin interface has the hability to edit more than one model
on a single page. This is know as inlines
'''
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

'''
we register them into admin so we can edit them if necessary
'''
admin.site.register(Order, OrderAdmin)


