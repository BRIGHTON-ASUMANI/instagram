from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = Post(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = current_user
            post.save()
        return redirect('NewsToday')

    else:
        form = NewArticleForm()
    return render(request, 'post.html', {})
