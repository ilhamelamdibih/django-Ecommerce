from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_home, name='product_home'),
    path('products', views.product_list, name='product_list'),
    path('productScrapped', views.detailScrapping, name='product_scrapp'),
    path('profile', views.profile, name='profile'),
    path('<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
        name='product_detail'),
    ]