from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from os_file_hoster.apps.file_manager import views

urlpatterns = patterns('',
    url(r'^file/upload/$', views.file_upload, name='file_upload'),
)
