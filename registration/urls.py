from django.conf.urls import  url
from registration import views

app_name = 'registration'

urlpatterns = [
    url(r'^$', views.register,                          										name='register'),
    url(r'^delegate/$', views.delegateRegister,         										name='delegateRegister'),
    url(r'^code/(?P<code>.+)$', views.studentRegister,  										name='studentRegister'),
    url(r'^success/(?P<profileType>.+)/(?:(?P<token>.+))?$', views.registerSuccess,				name='registerSuccess'),
    url(r'^change-infos', views.changeUserInfos,        										name='changeUserInfos'),
	url(r'^facebook/(?P<profileType>.+)/', views.registerUserFacebook,							name='registerUserFacebook'),
]