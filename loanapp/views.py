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
        if form.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
           
        return redirect('login')
    else:
        form= RegistrationForm()
    params={
        'form':form
    }
    return render(request, 'auth/signup.html', params)

def account(request,id):
    acc = Account.objects.get(id = id)
    return render(request,'user_account.html',{"account":acc})
    
@login_required(login_url='login')  
def updateaccount(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAccountUpdateForm(request.POST or None,request.FILES or None, instance=user.account)
        if form.is_valid():
            form.save()
            return redirect('account', request.user.id)
    else:
        form = UserAccountUpdateForm()
        return render(request, 'update_account.html',{"form":form })



