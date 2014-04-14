from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from os_file_hoster.apps.user_manager import views

urlpatterns = patterns('',
    url(r'^user/new/$', views.user_new, name='user_new'),
    url(r'^user/list/$', views.user_list, name='user_list'),
)
