from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField


# Create your models here.
class Subscribers(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Profile(models.Model):
    profile = models.ImageField(upload_to = 'profile/')
    bio = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    name = models.CharField(max_length=60)
    caption = HTMLField()
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ImageField(upload_to = 'posts/')
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def all_posts(cls):
        image = cls.objects.order_by('post_date')
        return image

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image


    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(profile__profile__icontains=search_term)
        return pictures
