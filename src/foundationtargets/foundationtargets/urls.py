from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # url(r'^$', 'myapp.views.myview', name='view_name'),
   
    (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),     

    url(
        r'^$',
        'django.views.generic.simple.direct_to_template',
        {
            'template':'base.html', 
        },
        name='home'
    ),
    url(
        r'^gecko-xml/(?P<slug>[\w-]+)/$', 
        'foundationtargets.views.gecko_xml', 
        {},
        name='gecko_xml'
    ), 
    url(
        r'^admin/foundationtargets/determinant-datapoints-edit/(?P<id>[\d-]+)/$', 
        'foundationtargets.views.determinant_datapoints_edit', 
        {},
        name='determinant_datapoints_edit'
    ), 

)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
