from django.conf.urls import patterns, include, url
from django.contrib import admin
from Core.views import *
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Core.views.home', name='home'),
    
    # url(r'^flats/(\w+)/(\w+)/$', 'Core.views.flats', name='flats'),
    url(r'^api/company/', 'Core.views.company', name='company'),
    url(r'^api/([\w ]+)/([\w ]+)/([\w ]+)/', 'Core.views.api3', name='api3'),
    url(r'^api/([\w ]+)/([\w ]+)/$', 'Core.views.area', name='area'),
    url(r'^api/([\w ]+)/$', 'Core.views.city_area', name='city_area'),
    
    url(r'^flats/([\w ]+)/([\w ]+)/([\w ]+)/$', 'Core.views.get_flats', name='get_flats'),
    url(r'^flats/', 'Core.views.flats', name='flats'),
    
    # url(r'^flats/', 'Core.views.filter', name='filter'),
    url(r'^admin/', include(admin.site.urls)),
)
