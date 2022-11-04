from django.shortcuts import render
from .models import Categories 
from product.models import Category,Product

# Create your views here.
def index(request):
    cat = Category.objects.all()

    trend = Product.objects.all()
    print(trend)

    context ={
        'cat':cat,
        'trend':trend,
    }

    return render(request,'home/index.html',context)

