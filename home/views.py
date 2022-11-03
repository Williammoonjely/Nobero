from django.shortcuts import render
from .models import Categories 
from product.models import Category,Product

# Create your views here.
def index(request):
    cat = Category.objects.all()
    return render(request,'home/index.html',{'cat':cat})