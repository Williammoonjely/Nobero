from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.views.generic import ListView
# Create your views here.

class Detail_view(ListView):
    model= Product
    template_name='categories.html'
def categories(request,id):
    
    category =Category.objects.get(id=id)   
    product = Product.objects.filter(category= category)
    print(product,'=====')
    return render(request,'product/categories.html',{'product':product})

    # else: 


    #     product = Product.objects.all()
    #     return render(request,'product/categories.html',{'product':product})

def product(request,id):
    products = Product.objects.get(id=id)
    print(product)
    
    return render(request,'product/product.html',{'products':products})