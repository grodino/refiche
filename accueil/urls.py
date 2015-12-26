# coding=UTF-8
from django.conf.urls import url
from accueil import views

app_name = 'accueil'

urlpatterns = [
	url(r'^about/$', views.about, name='about')
]