from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

import requests
import json


def product_home(request, category_slug=None):
    return render(request,'shop/product/home.html')

def detailScrapping(request):
    response_API = requests.get('http://localhost/scrapping_api/jewlerys.php')
    #print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    products=[]
    for i in parse_json['jewlers']:
        products.append({
            'name':i['name'],
            'price':i['price'],
            'img':i['img']
        })
    return render(request,'shop/product/listScrapp.html',{'products':products,'lenProd':len(products)})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                'shop/product/list.html',
                {'category': category,
                'categories': categories,
                'products': products,
                'lenProd':len(products)})

def profile(request):
    return render(request,'shop/profile.html',)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
    id=id,
    slug=slug,
    available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/product/detail.html',
    {'product': product,
     'cart_product_form': cart_product_form})