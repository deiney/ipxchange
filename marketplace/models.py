from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	category = models.CharField(max_length=50)

	def __unicode__(self):
		return self.category
	
#class User(models.Model):
#	username = models.CharField(max_length=200)
#	first = models.CharField(max_length=200)
#	last = models.CharField(max_length=200)
#	email = models.EmailField()
#	joined_dt = models.DateTimeField('date joined')
#	is_seller = models.BooleanField(default=False)
#
#	def __unicode__(self):
#		return self.first + ' ' + self.last

class UserStats(models.Model):
	user = models.ForeignKey(User)
	
	def username(self):
		return self.user.username
		
	def first_name(self):
		return self.user.first_name
	
	def last_name(self):
		return self.user.last_name
	
	def num_items(self):
		return (self.user.item_set.count())
	
	def is_seller(self):
		return self.num_items() > 0
	
	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name
	

class Item(models.Model):
	category = models.ForeignKey(Category)
	seller = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=5000)
	image = models.FileField(upload_to='items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __unicode__(self):
		return self.title

class Transaction(models.Model):
	buyer = models.ForeignKey(User, related_name='items_purchased')
	seller = models.ForeignKey(User, related_name='items_sold')
	item = models.ForeignKey(Item)
	trans_dt = models.DateTimeField('transaction date')
	
	def __unicode__(self):
		return `self.trans_dt` + '(item:' + `item` + ')'


class ItemReview(models.Model):
	item = models.ForeignKey(Item)
	reviewer = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=5000)
	created_dt = models.DateTimeField('review date')
	
	def __unicode__(self):
		return self.title


