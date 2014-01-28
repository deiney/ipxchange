from django.contrib import admin
from marketplace.models import UserStats, Item, Transaction, ItemReview, Category

class ItemInline(admin.TabularInline):
	model = Item
	extra = 1

class UserStatsAdmin(admin.ModelAdmin):
#	fieldsets = [
#		(None, {'fields': ['username']}),
#		('Details', {'fields':['first_name','last_name'], 'classes': ['collapse']}),
#	]
###	inlines = [ItemInline]
	list_display = ('username', 'first_name', 'last_name', 'is_seller')


admin.site.register(UserStats, UserStatsAdmin)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(ItemReview)
