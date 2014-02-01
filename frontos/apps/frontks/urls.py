from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from frontos.apps.frontks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/user/$', views.user_show, name='user'),
    url(r'^/user/login$', views.user_login, name='login'),
    url(r'^/user/create/$', views.user_create, name='user_create'),
    url(r'^/user/delete/$', views.user_delete, name='user_delete'),
    url(r'^/files/new/$', views.file_new, name='file_new'),
)
