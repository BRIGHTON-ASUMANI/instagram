from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField


# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_caption = TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    image_name = models.CharField(max_length=60)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')

    def __str__(self):
        return self.image_name

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        post = cls.objects.filter(pub_date__date = today)
        return post
