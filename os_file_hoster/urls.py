from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'', include('os_file_hoster.apps.file_manager.urls')),
    url(r'', include('os_file_hoster.apps.user_manager.urls')),
    url(r'', include('openstack_auth.urls')),
)
