from django.conf.urls import patterns, include, url
from django.contrib import admin
from PhysicExam import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.home, name='My templates\home.html'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin', include(admin.site.urls)),

)
