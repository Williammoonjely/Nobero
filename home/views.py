from django.shortcuts import render
from product.models import Category,Product

# Create your views here.
def index(request):
    cat = Category.objects.all()

    trend = Product.objects.all()

    latest = Product.objects.order_by('-id')[0:6]

    context ={
        'cat':cat,
        'trend':trend,
        'latest':latest,
    }

    return render(request,'home/index.html',context)

