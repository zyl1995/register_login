from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls import patterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'register_login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^users/', include('use_profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
