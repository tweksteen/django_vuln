from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'sql_injection/index.html'}),
    (r'^basic$', 'sql_injection.views.basic'),    
    (r'^advanced$', 'sql_injection.views.advanced'),    
    
)
