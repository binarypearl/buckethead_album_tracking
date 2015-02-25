from django.conf.urls import patterns, include, url

from django.http import HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buckethead_album_tracking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', lambda r: HttpResponseRedirect('batapp/')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^batapp/', include('batapp.urls', namespace="batapp")),
)
