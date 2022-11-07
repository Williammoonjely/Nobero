from unicodedata import category
from django.urls import path
from . import views

urlpatterns = [
    
    # path('categories',views.categories, name = 'cate'),
    path('categories/<int:id>',views.categories, name = 'categories'),
    path('product/<int:id>',views.product,name = 'product'),
]

