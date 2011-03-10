from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    #('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',
    # {'template': 'home.html'}),
    
    # For the passages
    (r'^$', 'passages.views.index'),
    (r'^new/$', 'passages.views.new'),
    (r'^ajax_lookup/$', 'passages.views.ajax_lookup'),
    
    
    # For the admin section
    (r'^admin/', include(admin.site.urls)),
)
