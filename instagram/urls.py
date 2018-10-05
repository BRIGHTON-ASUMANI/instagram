from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.auth, name='auth'),
    url('login/', views.login_user, name='login'),
]
