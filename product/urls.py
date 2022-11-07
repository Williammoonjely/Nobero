from unicodedata import category
from django.urls import path
from . import views


urlpatterns = [
    path('categories',views.categories, name = 'categories'),
    path('product',views.product,name = 'product'),
]

