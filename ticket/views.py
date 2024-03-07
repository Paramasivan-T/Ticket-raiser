from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .decoraters import *


# Create your views here.
@login_required(login_url='login/')
def home(request):
    user = get_object_or_404(User, id=request.user.id)
    
    # To check and redirect the developer to dev page
    if request.user.groups.filter(name='Developer').exists():
        return redirect('dev')
    
    # To check and redirect the admin to admin_dashboard page
    if request.user.groups.filter(name='Admin').exists():
        return redirect('admin_dashboard')
    
    # To add every new user to general group
    admin_group = Group.objects.get(name='General')
    user.groups.add(admin_group)
    
    project_objects = Project.objects.all()

    context={'project_objects': project_objects}
    return render(request, 'ticket/home.html',context=context)


@unauthenticated_user
def createUser(request):

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


@login_required(login_url='login/')
def logoutUser(request):
    logout(request)
    return redirect('login')


@developer_required
def developer_dashboard(request):

    context = {}
    return render(request, 'ticket/dev.html', context)


@admin_required
def admin_dashboard(request):
    
    context = {}
    return render(request, 'ticket/admin_view.html', context)


@login_required(login_url='login/')
def details(request, id):
    project_object = Project.objects.get(id=id)
    
    if request.method == 'POST':
        form = TickeRaisingForm(request.POST, request.FILES)
        
        if form.is_valid():
            ticket_form = form.save(commit=False)
            ticket_form.created_by = request.user
            ticket_form.project = project_object
            ticket_form.save()
            messages.success(request, "Ticket Submitted Successfully")
            # return redirect('home')
    else:
        form = TickeRaisingForm()

    context = {'project_object': project_object, 'form': form}
    return render(request, "ticket/details.html", context)