from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^frontks', include('frontos.apps.frontks.urls', namespace="frontks")),
    url(r'', include('openstack_auth.urls')),
)
