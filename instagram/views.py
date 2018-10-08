from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SubForm
from .models import Image, Profile
import datetime as dt
from .email import send_welcome_email

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    image=Image.all_posts()
    date = dt.date.today

    return render(request, 'index.html',{'date': date, 'image': image})


@login_required(login_url='/accounts/login/')
def today_post(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = Subscribers(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('today_post')
    else:
        form = SubForm()
    return render(request, 'today.html', {"date": date,"news":news,"SubForm":form})



# @login_required(login_url='/accounts/login/')
# def post(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = Post(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.posted_by = current_user
#             post.save()
#         return redirect('NewsToday')
#
#     else:
#         form = NewArticleForm()
#     return render(request, 'post.html', {})
