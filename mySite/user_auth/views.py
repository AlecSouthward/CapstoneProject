from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def user_login(request):
    """This renders the  login.html page."""
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """This will either render the login page,
        or will send the user to the index page.

        It will decide which after checking if the user
        is logged in and a valid user.
    """

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
    """This is a testing page used to see the
        users name and encrypted password.
    """

    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def create_user(request):
    """This will render the create_user.html (the user register) page."""

    return render(request, 'authentication/create_user.html')

def reg_user(request):
    """This will either render the create_user.html (the user register) page,
        or will send the user to the index page.

        It will create a User object based on what the user
        input on the page.

        After checking if the User object is valid it will send the user
        back to the index page, otherwise it will send the user back
        to the register page.
    """

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