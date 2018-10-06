from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    post = HTMLField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/', blank = True)

    def __str__(self):
        return self.title
