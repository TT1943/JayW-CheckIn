from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'checkin.views.home', name='home'),
    url(r'^post$', 'checkin.views.post', name='post'),
    url(r'^event/(?P<event_id>\d+)$', 'checkin.views.info', name='info'),
    url(r'^event/(?P<event_id>\d+)/create_contact$', 'checkin.views.create_contact', name='create_contact'),
    url(r'^check/(?P<event_id>\d+)/(?P<contact_id>\d+)$', 'checkin.views.check', name='check'),
    url(r'^uncheck/(?P<event_id>\d+)/(?P<contact_id>\d+)$', 'checkin.views.uncheck', name='uncheck'),
    # url(r'^jayw/', include('jayw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
