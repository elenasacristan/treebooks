from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_urls
from home import urls as home_urls
from home.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^home/', include(home_urls)),
]
