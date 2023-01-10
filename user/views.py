from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserForm


def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registertion')
    context={'form':form}
    return render(request,'user_register/register_login.html',context)


def login_user(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or Password Doest Not Exits')

    context= {'page': page}
    return render(request,'user_register/register_login.html',context)


def logout_user(request):
    logout(request)
    return redirect ('home')
