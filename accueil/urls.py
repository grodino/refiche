# coding=UTF-8
from django.conf.urls import patterns, url

urlpatterns = patterns('accueil.views',
	url(r'^about/$', 'about')
)