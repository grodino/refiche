from django.conf.urls import patterns, url

urlpatterns = patterns('facebook.views',
	url(r'^create-group/(?P<tokenValue>.+)/(?P<facebookUserId>.+)$', 'createClassroomGroup'),
)