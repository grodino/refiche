from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'refiche.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^', include('accueil.urls')),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'accueil/login_accueil.html'}),
    url(r'^app/', include('app.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^register/', include('registration.urls')),
]
