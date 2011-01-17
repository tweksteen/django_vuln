from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template':'path_traversal/index.html'}),
    (r'^basic$', 'path_traversal.views.basic'), 
    (r'^advanced$', 'path_traversal.views.advanced'),      
         
)
