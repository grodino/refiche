from django.conf.urls import patterns, url

urlpatterns = patterns('registration.views',
    url(r'^$', 'register'),
    url(r'^delegate/$', 'delegateRegister'),
)