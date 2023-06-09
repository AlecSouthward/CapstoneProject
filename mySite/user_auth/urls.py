from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
name='authenticate_user'),

    path('show_user/', views.show_user, name='show_user'),

    path('create_user/', views.create_user, name='create_user'),
    path('reg_user/', views.reg_user, name='reg_user')
]