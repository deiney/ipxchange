from django.conf.urls import patterns, url

from marketplace import views

urlpatterns = patterns('',
	# url(regex, view, kwargs, name)
	#      (name value, as called by the {% url %} template tag)
    # Examples:
    # url(r'^$', 'ipxchange.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^$', views.index, name='index'),
	url(r'^users/$', views.UsersIndex.as_view(), name='users'),
#	url(r'^user/(?P<pk>\d+)/$', views.UserView.as_view(), name='user_detail'),
	
	url(r'^user/(?P<pk>\d+)/$', views.user_details, name='user_detail'),
#	url(r'^\?q=(?P<query>\.+)', views.SearchResults.as_view(), name='search_results'),
	url(r'^search/$', views.search_results, name='search_results'),

	
#	url(r'^media/', views.image, name='image'),
	
#	url(r'^users/(?P<pk>\d+)/$', views.UsersView.as_view(), name='users'),
#	url(r'^user/(?P<pk>\d+)/$', views.DetailView.as_view(), name='user'),
#	url(r'^user/(?P<pk>\d+)/catalog/$', views.vote, name='user_catalog'),
#	url(r'^item/(?P<pk>\d+)/$', views.DetailView.as_view(), name='item'),
	
#	url(r'^$', views.index, name='index'),
#	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
