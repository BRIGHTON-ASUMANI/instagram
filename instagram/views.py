from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, PostForm, CommentForm
from django.contrib.auth.models import User
from .models import Image, Comments
import datetime as dt

# Create your views here.

def home(request):
    image=Image.all_images()
    date = dt.date.today
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         content = form.cleaned_data['content']
    #         recepient  = Comments(content=content)
    #         recepient.save()
    #         HttpResponseRedirect('home')
    # else:
    #     form = CommentForm()
    return render(request, 'home.html',{'date': date, 'image': image})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in' ))
            return redirect('home')
        else:
            messages.success(request, ('error logging in - please try again' ))
            return redirect('login')
    else:
        return render(request, 'login.html', {} )

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out' ))
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered' ))
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'register.html',context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form }
    return render(request, 'edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have password has been changed' ))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form }
    return render(request, 'change_password.html',context)

@login_required
def profile(request):
    # image=Image.all_images()
    date = dt.date.today
    profiles = Profile.objects.filter(id = profile_id)
    return render(request, 'profile.html',{'date': date, 'image': image})



def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'home.html', {"form": form})
