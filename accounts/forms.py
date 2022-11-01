from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):

    lastname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    # password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ('name','email')
        

