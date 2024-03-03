from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='login/')
def home(request):
    project_objects = Project.objects.all()

    context={'project_objects': project_objects}
    return render(request, 'ticket/home.html',context=context)


def createUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account Successfully created for {username}')
                return redirect('login')

    context = {'form':form}
    return render(request, 'ticket/signup.html',context=context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)

            if user is not None:
                login(request,user)
                return redirect('home')
            
            else:
                messages.info(request,'Username or Password is incorrect')

    context={}
    return render(request, 'ticket/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')