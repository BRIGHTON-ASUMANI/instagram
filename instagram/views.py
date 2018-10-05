from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def auth(request):
    return render(request, 'auth/register.html', {})
