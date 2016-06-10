from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bugs_detector0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get_count', 'www.views.get_count'),
    url(r'^.*', 'www.views.home'),
    # url(r'^admin/', include(admin.site.urls)),
)
