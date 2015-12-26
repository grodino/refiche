# coding=UTF-8
from django.conf.urls import  url
from app import views

app_name = 'app'

urlpatterns = [
	url(r'^home/$', views.home, 											name='home'),
	url(r'^lesson/(?P<lesson_name>.+)$', views.lessonPage, 					name='lessonPage'),
	url(r'^feed/$', views.classroomSheetsFeed, 								name='classroomSheetsFeed'),
	url(r'^upload/$', views.newSheetPage, 									name='newSheetPage'),
	url(r'^download/(?P<pk>\d+)$', views.downloadSheetPage, 				name='downloadSheetPage'),
	url(r'^sheet/delete/(?P<pk>\d+)$', views.deleteSheetPage, 				name='deleteSheetPage'),
	url(r'^link/delete/(?P<pk>\d+)$', views.deleteLinkPage, 				name='deleteLinkPage'),
	url(r'^classroom/$', views.classroomPage, 								name='classroomPage'),
	url(r'^account/$', views.accountPage, 									name='accountPage'),
	url(r'^media/(?P<ressource>.+)/(?P<url>.+)$', views.downloadRessource, 	name='downloadRessource'),
	url(r'^link/$', views.newLinkPage, 										name='newLinkPage'),
	url(r'^test/$', views.underConstruction, 								name='underConstruction')
]