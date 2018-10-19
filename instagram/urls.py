from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from . import views


urlpatterns=[
    url(r'^home/',views.home,name='home'),
    url(r'^$',views.login_user, name='login'),
    url('logout/',views.logout_user, name='logout'),
    url('register/',views.register_user, name='register'),
    url('profile/',views.profile, name='profile'),
    url('edit_profile/',views.edit_profile, name='edit_profile'),
    url('change_password/',views.change_password, name='change_password'),
    url(r'^post/$', views.new_image, name='new_image'),
    url('edit/',views.edit, name='edit'),
    url(r'^comments/(\d+)', views.comment, name='comments'),
    url( r'^newprofile/$' , views.newprofile , name='newprofile' ),#newprofile is the same as createprofile
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
