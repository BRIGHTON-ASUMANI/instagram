from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.index, name='index'),
    url('^post/', views.post, name='post'),
]
