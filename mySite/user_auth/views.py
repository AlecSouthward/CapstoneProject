from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('index')
        )
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def create_user(request):
    return render(request, 'authentication/create_user.html')

def reg_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.create_user(username, '', password)
    user.first_name = username
    user.save()
    
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:create_user')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('index')
        )