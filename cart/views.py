from django.shortcuts import render

# Create your views here.

def orders(request):
    return render(request,'cart/orders.html')
def address(request):
    return render(request,'cart/address.html')
def payment(request):
    return render(request,'cart/payment.html')
def confirm(request):
    return render(request,'cart/confirm.html')