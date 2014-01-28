from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# url(regex, view, kwargs, name)
	#      (name value, as called by the {% url %} template tag)
    # Examples:
    # url(r'^$', 'ipxchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^marketplace/', include('marketplace.urls', namespace="marketplace")),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
