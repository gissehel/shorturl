from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^u/(?P<name>[^/]+)$', 'urllink.views.link'),
]
