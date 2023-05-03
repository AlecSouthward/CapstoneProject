from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:15]
    user_auth = request.user.is_authenticated

    if request.user.is_authenticated: 
        user_name = request.user.first_name
    else: 
        user_name = ''

    context = {'latest_post_list': latest_post_list, 'user_logged_in':user_auth, 'user_name':user_name}
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def songs(request):
    return render(request, 'songs.html')