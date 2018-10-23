from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.urlresolvers import reverse

class Profile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    prof_pic = ImageField()
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('lump', kwargs={'pk':self.pk})


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user.username

    @classmethod
    def update_caption(cls,default,update):
        fetched = Profile.objects.filter(name=default).update(name=update)
        return fetched

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
    image = ImageField()
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes=models.PositiveIntegerField( default=0)


    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk':self.pk})

    @classmethod
    def save_image(self):
        self.save()
    @classmethod
    def get_images(cls):
         images = cls.objects.all()
         return images
    @classmethod
    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pic = cls.objects.filter(pk=id)
        pic.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pic = cls.objects.get(pk=id)
        return pic



    def __str__(self):
        return self.image_name


    @classmethod
    def all_images(cls):
        image = cls.objects.order_by('image_date')
        return image

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def update_caption(cls,default,update):
        fetched = Image.objects.filter(name=default).update(name=update)
        return fetched

    @classmethod
    def save_image(self):
        return self.save()

    @classmethod
    def delete_image(self):
        return self.delete()

class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.CharField(max_length =300)
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
