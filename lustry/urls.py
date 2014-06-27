from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
#    url(r'^auth/', include('loginsys.urls')),  # переадресовываем все заросы в loginsys.urls
     url(r'^', include('shop.urls')),  # переадресовываем все заросы в shop.urls
)
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
