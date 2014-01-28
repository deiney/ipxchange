from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone
from django.db.models import Q

from marketplace.models import User, Item, Category, ItemReview, Transaction
from marketplace.forms import SearchForm

# homepage
def index(request):
	form = SearchForm()
	return render(request, 'marketplace/index.html', {'form':form})
		

# List of users	
class UsersIndex(generic.ListView):
	# overwrite default template: <app name>/<model name>_list.html
	template_name = 'marketplace/users.html'
	# overwrite default 'user_list'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		"""
		Return all users, sorted by id
		"""
		return User.objects.all()

# User details page - ver. 1		
def user_details(request, pk):
	user = User.objects.get(pk=pk)
	output = "user id = %s" % user.pk
	return render(request, 'marketplace/user_detail.html', {'user':user})

# User details page - ver. 2	
class UserView(generic.DetailView):
	model = User
	# keep default context variable 'user'
	#context_object_name = 'user'
	# overwrite default template: <app name>/<model name>_detail.html
	#template_name = 'marketplace/user_detail.html'

def search_results(request):
	form = SearchForm(request.GET)
	if form.is_valid():
		query = form.cleaned_data['q']
	else:
		return render(request, 'marketplace/index.html', {'form':form})
#	query = ''
	results = []
	try:
		query = request.GET['q']
		if len(query) > 0:
			results = Item.objects.filter(Q(title__contains=query) | Q(description__contains=query))
	except (NameError, KeyError):
		return render(request, 'marketplace/search_results.html', {'query':query, 'resuts':results, 'error_message': "No results found",})
	else:
		return render(request, 'marketplace/search_results.html', {'query':query, 'results':results})



