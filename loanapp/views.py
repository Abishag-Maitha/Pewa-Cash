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

def account(request,id):
    acc = Account.objects.get(id = id)
    return render(request,'user_account.html',{"account":acc})

def updateaccount(request):
    user= request.user
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        acc_form = UserAccountUpdateForm(request.POST, request.FILES, instance=request.user.account)
        if user_form.is_valid() and  acc_form.is_valid():
            user_form.save()
            acc_form.save()
            return redirect('account', user.id)
    else:
        user_form = UserUpdateForm(instance=request.user)
        acc_form = UserAccountUpdateForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'acc_form': acc_form
    }
    return render(request, 'update_account.html', params)
    