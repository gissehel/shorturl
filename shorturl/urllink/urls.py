from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<name>[^/]+)$', views.link),
]
