from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'ticket/home.html')


def CreateUser(request):
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


def LoginUser(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')
        # user = authenticate(request, username=username)

    return render(request, 'ticket/login.html')

