from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'xss/index.html'}),
    (r'^basic$', 'xss.views.basic'),   
    (r'^stripped$', 'xss.views.stripped'),
    (r'^js_based$', 'xss.views.js_based'),    
    (r'^dom_based$', 'xss.views.dom_based'),    
)
