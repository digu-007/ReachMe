from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import UserInfo
from .forms import CreateUserForm, CreateUserInfoForm


@login_required(login_url='login')
def homePage(request):
    """User will see recommendations of other users here"""
    context = {
        "recommendations": UserInfo.objects.all()
    }
    return render(request, 'user/home.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)

            messages.success(request, 'Account was created for ' + username)
            return redirect('settings')

    context = {'form': form}
    return render(request, 'user/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'user/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboardPage(request):
    return render(request, 'user/dashboard.html')


@login_required(login_url='login')
def settingsPage(request):
    form = CreateUserInfoForm(initial={'user': request.user})

    if request.method == 'POST':
        form = CreateUserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'user/settings.html', context)
