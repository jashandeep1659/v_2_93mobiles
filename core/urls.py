from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('all/', views.all_list, name="all_list"),
    path('deals/', views.all_deals, name="deals"),
    path('all_series/', views.all_series, name="all_series"),
    path('series/<str:slug>/',views.iPhone_series_wise , name="series_iphone"),
    path('list/<str:slug_list>/',views.iphones_list, name="list"),
    path('check/<int:id_product>/<str:slug_product>', views.product_view, name="product_view"),
]
