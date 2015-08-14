from django.conf.urls import patterns, url

urlpatterns = patterns('registration.views',
    url(r'^$', 'register'),
    url(r'^get-student-code/', 'getCode'),
    url(r'^delegate/$', 'delegateRegister'),
    url(r'^code/(?P<code>.+)$', 'studentRegister'),
)