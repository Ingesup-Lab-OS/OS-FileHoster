from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from os_file_hoster.apps.file_manager import views

urlpatterns = patterns('',
    url(r'^upload/$', views.file_upload, name='file_upload'),
    url(r'^list/$', views.file_list, name='file_list'),
    url(r'^list/(?P<container>\w+)/$', views.file_list, name='file_list'),
    url(r'^delete/(?P<name>.+)/(?P<container>\w+)$', views.file_delete, name='file_delete'),
)
