from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomerSignUp
from django import forms


class CustomerSignUpForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateCustomerForm(forms.ModelForm):
  
    information = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CustomerSignUp
        exclude = ['user']
