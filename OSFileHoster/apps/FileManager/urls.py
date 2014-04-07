from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from OSFileHoster.apps.FileManager import views

urlpatterns = patterns('',
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^session_auth_token/$', views.session_auth_token, name='session_auth_token'),
)
