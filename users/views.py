from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from .form import Login
# Create your views here.

def index(request):
    # whether the user is authenticated
    if request.user.is_authenticated:
        return render(request, 'users/index.html')
    else:
        return HttpResponseRedirect(reverse('users:login'))
    

def login_view(request):
    # initail the form
    form = Login()
    # if the request.method == 'POST'
    if request.method == 'POST':
        # use the request.POST content fill the form
        form = Login(request.POST)
        # wether the form is valid
        if form.is_valid():
            # get the data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # login the user
                login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            else:
                return render(request, 'users/login.html', {
                    'form': form,
                    'message': 'Invalid ID',
                })
    return render(request, 'users/login.html', {
        'form': form
    })

def logout_view(request):
    # first to logout
    logout(request)
    # because here we need to sent a message, so we don't use HttpResponseRedirect(reverse('users:login'))
    form = Login()
    return render(request, 'users/login.html', {
        'form': form,
        'message': 'Log out'
    })
