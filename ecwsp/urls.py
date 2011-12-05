from django.conf.urls.defaults import *
from ecwsp.sis.views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include("massadmin.urls")),
    (r'^admin_export/', include("admin_export.urls")),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^$', 'ecwsp.sis.views.index'),

    (r'^sis/', include('ecwsp.sis.urls')),
    
    (r'^accounts/password_change/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done'),
    (r'^logout/$', logout_view),
  #  (r'^chart/$',chart_fte),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    (r'^admin/', include(admin.site.urls) ),
    (r'^ldap_grp/', include('ldap_groups.urls')),
    (r'^ajax_select/', include('ajax_select.urls')),
    (r'^ajax_filtered_fields/', include('ajax_filtered_fields.urls')),
)

if settings.GAPPS:
    urlpatterns += patterns('', (r'^accounts/login/$', 'ecwsp.google_auth.views.login'), )
else:
    urlpatterns += patterns('', (r'^accounts/login/$', 'django.contrib.auth.views.login'), )

if 'ecwsp.schedule' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^schedule/', include('ecwsp.schedule.urls')), )
if 'ecwsp.work_study' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^work_study/', include('ecwsp.work_study.urls')), )
if 'ecwsp.admissions' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^admissions/', include('ecwsp.admissions.urls')), )
if 'ecwsp.omr' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^omr/', include('ecwsp.omr.urls')), )
if 'ecwsp.volunteer_track' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^volunteer_track/', include('ecwsp.volunteer_track.urls')), )
if 'ecwsp.benchmark_grade' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^benchmark_grade/', include('ecwsp.benchmark_grade.urls')), )
if 'ecwsp.inventory' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^inventory/', include('ecwsp.inventory.urls')), )
if 'ecwsp.engrade_sync' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', (r'^engrade_sync/', include('ecwsp.engrade_sync.urls')), )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,})
    )

if settings.CAS:
    urlpatterns += patterns('',
        (r'^accounts/login/$', 'django_cas.views.login'),
        (r'^accounts/logout/$', 'django_cas.views.logout'),
    )
