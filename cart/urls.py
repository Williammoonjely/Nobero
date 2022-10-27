from django.urls import path
from . import views

urlpatterns = [
    path('orders/',views.orders, name = 'orders'),
    path('address/',views.address,name = 'address'),
    path('payment/',views.payment, name = 'payment'),
    path('confirm/',views.confirm, name = 'confirm'),
]
