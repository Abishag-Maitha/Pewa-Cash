from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import AccountForm,UserUpdateForm,RegistrationForm,UserAccountUpdateForm,LoanForm,PaymentForm
from .models import Account, Loan, Payment
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def signup(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=AccountForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            account=procForm.save(commit=False)
            account.user=user
            account.save()

        return redirect('login')
    else:
        form= RegistrationForm()
        prof=AccountForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'auth/signup.html', params)