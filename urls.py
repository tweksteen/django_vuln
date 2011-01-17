import settings
from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', 
            {'template':'index.html', 
             'extra_context':
                {'apps_index': [s + "/index.html" for s in settings.WEAK_APPS]}
            }),
    (r'^sql_injection/', include('django_vuln.sql_injection.urls')),
    (r'^xpath_injection/', include('django_vuln.xpath_injection.urls')),
    (r'^path_traversal/', include('django_vuln.path_traversal.urls')),
    (r'^xss/', include('django_vuln.xss.urls')),
    (r'^admin/', include(admin.site.urls)),
)
