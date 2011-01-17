from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'xpath_injection/index.html'}),
    (r'^basic$', 'xpath_injection.views.basic'),        
)
