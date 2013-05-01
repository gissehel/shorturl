from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^shorturl/', include('shorturl.foo.urls')),
    #r'^u/', include('shortu
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^admin/', include(admin.site.urls)),
    (r'^u/(?P<name>[^/]+)$', 'urllink.views.link'),
)
