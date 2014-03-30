from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from frontos.apps.frontks import views

urlpatterns = patterns('',
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
)
