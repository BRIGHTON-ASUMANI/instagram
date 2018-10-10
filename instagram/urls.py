from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import (createpost, detail_post_view, postpreference)


urlpatterns=[
    url(r'^create/', views.createpost, name='createpost'),
    url(r'^(?P<id>\d+)/$', views.detail_post_view, name='detail'),
    url(r'^(?P<postid>\d+)/preference/(?P<userpreference>\d+)/$', views.postpreference, name='postpreference'),
    url('home/',views.home,name='home'),
    url('^$',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('profile/',views.user_profile, name='profile'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
    url('profile/',views.user_profile, name='profile'),
]
