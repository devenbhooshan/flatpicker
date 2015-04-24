from django.conf.urls import patterns, include, url
from django.contrib import admin
from Core.views import *
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Core.views.home', name='home'),
    url(r'^flats/(\w+)/(\w+)/$', 'Core.views.flats', name='flats'),
    url(r'^admin/', include(admin.site.urls)),
)
