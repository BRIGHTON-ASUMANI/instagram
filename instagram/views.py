from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ImageForm, CommentForm, ProfileForm
from django.contrib.auth.models import User
from .models import Image, Comment, Profile
import datetime as dt
from .email import send_welcome_email
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View


# Create your views here.
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


def home(request):
    profile = Profile.get_all()
    image=Image.objects.filter()
    current_user = request.user
    commented = CommentForm()
    #comments = Comment.all_comments()
    context = {"image":image,"current_user":current_user,"profile":profile, 'commented':commented}

    return render(request, 'home.html',context)

@login_required(login_url='/login')
def comment(request,id):
    upload = Image.objects.get(id=id)
    if request.method == 'POST':
        comm=CommentForm(request.POST)
        if comm.is_valid():
            comment=comm.save(commit=False)
            comment.user = request.user
            comment.post=upload
            comment.save()
            return redirect('home')
    return redirect('home')

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
            send_welcome_email(username, user.email)
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'register.html',context)

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
    return render(request, 'change_password.html', context)

@login_required(login_url='/login')
def profile(request):
    profile =Profile.objects.filter(user=request.user.id)
    image =Image.objects.filter(user=request.user.id)
    commented = CommentForm()
    return render(request, 'profile.html', {"profile": profile, "image": image})

@login_required( login_url='/login' )
def newprofile(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'newprofile.html' , {"form": form} )


def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user, data=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'edit_profile.html',context)
#
# # @login_required( login_url='/accounts/login/' )
# def edit(request):
#   current_user=request.user
#   if request.method == 'POST':
#     form=ProfileForm( request.POST , request.FILES )
#     if form.is_valid( ):
#       update=form.save( commit=False )
#       update.user=current_user
#       update.save( )
#       return redirect( 'profile' )
#   else:
#     form=ProfileForm( )
#   return render( request , 'edit.html' , {"form": form} )

@login_required(login_url='/login')
def lump(request,pk):
    profile =Profile.objects.filter(user=request.user.id)
    project =Project.objects.filter(user=request.user.id)
    commented = CommentForm()
    return render(request,'lump.html',{"profile": profile, "project": project})
