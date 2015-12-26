from django.conf.urls import url
from facebook import views


urlpatterns = [
	url(r'^create-group/(?P<tokenValue>.+)/(?P<facebookUserId>.+)$', views.createClassroomGroup, name='createClassroomGroup'),
]