from django.shortcuts import render
from .models import Categories 
from product.models import Category,Product

# Create your views here.
def index(request):
    cat = Category.objects.all()

    trend = Product.objects.all()

    latest = Product.objects.order_by('-id')

    context ={
        'cat':cat,
        'trend':trend,
        'latest':latest,
    }

    return render(request,'home/index.html',context)

