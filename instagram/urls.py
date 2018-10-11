from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns=[
    url('home/',views.home,name='home'),
    url('^$',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    # url('profile/',views.user_profile, name='profile'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
    url('post/', views.new_post, name='new_post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
