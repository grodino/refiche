from django.conf.urls import url
from facebook import views

app_name = 'facebook'

urlpatterns = [
	url(r'^create-group/(?P<tokenValue>.+)/(?P<facebookUserId>.+)$',
		views.createClassroomGroup, name='createClassroomGroup'),
	url(r'^login/', views.facebook_login, name='login')
]