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
    url('edit_profilic/',views.edit_profilic, name='edit_profilic'),
    url('change_password/',views.change_password, name='change_password'),
    url(r'^post/$', views.new_image, name='new_image'),
    url(r'^comments/(\d+)', views.comment, name='comments'),
    url( r'^newprofile/$' , views.newprofile , name='newprofile' ),#newprofile is the same as createprofile
    url( r'pro/(?P<pk>[0-9]+)/$' , views.lump, name='lump' ),
    url( r'project/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view( ) , name='album-update' ) ,
    url( r'prof/(?P<pk>[0-9]+)/$' , views.ProfileUpdate.as_view( ) , name='profile-update' ) ,
    url( r'project/(?P<pk>[0-9]+)/delete/$' , views.AlbumDelete.as_view( ) , name='album-delete' ) ,
    url( r'profile/(?P<pk>[0-9]+)/delete/$' , views.ProfileDelete.as_view( ) , name='profile-delete' ) ,
    url( r'^create/$' , views.create , name='create' ),
    url( r'^like/(?P<up>.+)/(?P<pk>\d+)' , views.like , name='like' ),
    url(r'^search',views.search_results,name='search'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
