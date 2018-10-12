from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
# from django.db.models.signals import post_save
from django.utils import timezone

User = get_user_model()

class Profile(models.Model):
    prof_pic = ImageField(manual_crop = '150x150')
    bio = models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')



    def __str__(self):
        return self.user.username
    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def save_profile(self):
        return self.save()

    @classmethod
    def delete_profile(self):
        return self.delete()
class Image(models.Model):
    user = models.ForeignKey(User, related_name="editor", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/', blank=True)
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name


    @classmethod
    def all_images(cls):
        image = cls.objects.order_by('post_date')
        return image

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image


    @classmethod
    def save_image(self):
        return self.save()

    @classmethod
    def delete_image(self):
        return self.delete()

class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    @classmethod
    def all_comments(cls):
        comments = cls.objects.all()
        return comments


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)
