from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
	series = Series.objects.all()[:6]
	latest_products = Product.objects.all()[:6]
	latest_deals = Produts_Offers.objects.all()[:6]

	context = {
	'series':series,
	'latest_products':latest_products,
	'latest_deals':latest_deals,
	}
	return render(request, 'core/index.html', context)

def iPhone_series_wise(request, slug):
	series = iPhone_Name.objects.all()
	serie = get_object_or_404(Series,slug=slug)

	context ={
	'serie':serie,
	'series':series
	}
	return render(request, 'core/series_iphone.html',context)

def iphones_list(request, slug_list):
	iphones = Product.objects.all()
	serie = get_object_or_404(iPhone_Name,slug=slug_list)

	context = {
	'iphones':iphones,
	'serie':serie,
	}
	return render(request, 'core/iphones.html', context)

def product_view(request, id_product , slug_product):
	product = get_object_or_404(Product , id=id_product )
	product_images = other_product_images.objects.all()
	# latest_products = Product.objects.all().exclude(id = product.id)
	latest_products = Product.objects.all()
	context = {
	'product':product,
	'product_images':product_images,
	'latest_products': latest_products,
	}
	return render(request, 'core/product/product.html', context)

def all_list(request):
	product_show = Product.objects.all()
	context = {
	'product_show':product_show,
	}
	return render(request, 'core/product/all.html', context)

def all_deals(request):
	latest_products = Product.objects.all()
	latest_deals = Produts_Offers.objects.all()
	context = {
	'latest_products':latest_products,
	'latest_deals':latest_deals,
	}
	return render(request, 'core/product/deals.html', context)

def all_series(request):
	series = Series.objects.all()
	context ={
	'series':series
	}
	return render(request, 'core/product/series.html', context)
