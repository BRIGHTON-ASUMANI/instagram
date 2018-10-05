from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def auth(request):
    return render(request, 'auth/register.html', {})

def login_user(request):
    return render(request, 'auth/login.html', {})
