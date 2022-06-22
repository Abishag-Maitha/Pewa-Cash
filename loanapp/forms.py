from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Loan, Payment


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['Full_Name', 'MobileNo', 'ID_card']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email'] 

class UserAccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Account
        fields = ['email', 'photo', 'MobileNo']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['Loan_Amount','Loan_Term']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['Amount']
        
class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:

            user.save()
        return user