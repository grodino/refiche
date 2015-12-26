# coding=UTF-8
from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
	url(r'^home/$', 'home'),
	url(r'^lesson/(?P<lesson_name>.+)$', 'lessonPage'),
	url(r'^feed/$', 'classroomSheetsFeed'),
	url(r'^upload/$', 'newSheetPage'),
	url(r'^download/(?P<pk>\d+)$', 'downloadSheetPage'),
	url(r'^sheet/delete/(?P<pk>\d+)$', 'deleteSheetPage'),
	url(r'^link/delete/(?P<pk>\d+)$', 'deleteLinkPage'),
	url(r'^classroom/$', 'classroomPage'),
	url(r'^account/$', 'accountPage'),
	url(r'^media/(?P<ressource>.+)/(?P<url>.+)$', 'downloadRessource'),
	url(r'^link/$', 'newLinkPage'),
	url(r'^test/$', 'underConstruction')
)