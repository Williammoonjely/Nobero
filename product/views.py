from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product

# Create your views here.

def categories(request):
    product = Product.objects.all()
    print(product)
    return render(request,'product/categories.html',{'product':product})

def product(request):
    product = Product.objects.all()
    
    return render(request,'product/product.html',{'product':product})