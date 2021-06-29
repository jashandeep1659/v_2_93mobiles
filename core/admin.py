from django.contrib import admin

# Register your models here.
from .models import *


class product_images(admin.TabularInline):
	model  = other_product_images
	raw_id_fields =	['proudct_name']

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
	list_display = ['series_name','created_at']
	prepopulated_fields = {'slug': ('series_name',)}

@admin.register(iPhone_Name)
class iphone_nameAdmin(admin.ModelAdmin):
	list_display = ['iPhone_name']
	prepopulated_fields = {'slug': ('iPhone_name',)}
	list_filter = ('of_series',)

@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
	list_display = ['name','id','storage','battery_health','older_price','new_price','status']
	list_filter = ['storage','name','status',]
	search_fields = ['storage']
	prepopulated_fields = {'slug':('name',)}
	inlines = [product_images]

admin.site.register(Produts_Offers)
