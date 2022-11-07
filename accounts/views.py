from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm , RegistrationForm
from django.contrib.auth import login , authenticate , logout
# from .models import Profile
from django.contrib import messages
from product.models import Category,Product
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('thissisis sis s s sisre equest post data',request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # lastname = form.cleaned_data['lastname']

            # user_profile = Profile(
            #     lastname = lastname,
            #     user_id=user
            # )
            # user_profile.save()

            print(user)
            
            messages.success(request,'you have signed up successfully!')
            return redirect(reverse('home:index'))

        else:
            return render(request,'accounts/account.html', {'form':form})
    form = RegistrationForm()

    return render(request,'accounts/account.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            password = cd['password']
            user = authenticate(request,email = email,password = password)
            print(email,password)
            print(user)
            print(user.name)
            if user is not None:
                login(request,user)

                return redirect(reverse('home:index'))
            else:
                print('invalid credentials!')



    form = LoginForm()  
    registration = RegistrationForm()
    return render(request,'accounts/account.html', {'form':form,'regform':registration})

def signout(request):
    logout(request)
    return redirect(reverse('home:index'))


# def user(request):
#     return render(request,'accounts/account.html')
