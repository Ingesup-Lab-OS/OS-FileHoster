from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'', include('OSFileHoster.apps.FileManager.urls')),
    url(r'', include('openstack_auth.urls')),
)
