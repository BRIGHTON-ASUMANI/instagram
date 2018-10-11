from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.utils import timezone

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     prof_pic = models.ImageField(upload_to='profile/')
#
# # def create_profile(sender, **kwargs):
# #     if kwargs['created']:
# #         user_profile = UserProfile.objects.create(user=kwargs['instance'])
# #
# # post_save.connect(create_profile, sender=User)


    # def __str__(self):
    #     return self.user.username
    #
    # @classmethod
    # def get_profiles(cls):
    #     profiles = cls.objects.all()
    #     return profiles
    #
    #

class Image(models.Model):
    user = models.ForeignKey(User, related_name="editor", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='post/')
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    # like = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE, null=True)
    # profile = models.ForeignKey(User,on_delete=models.CASCADE)
    # likes =
    # comments =

    def __str__(self):
        return self.image_name


    @classmethod
    def all_images(cls):
        image = cls.objects.order_by('post_date')
        return image

    # @classmethod
    # def get_image(cls, id):
    #     image = cls.objects.get(id=id)
    #     return image

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

# class Comment(models.Model):
#     # comment = models.TextField(max_length=150)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments')
#     user = models.ForeignKey(User, related_name='comments_by', on_delete=models.CASCADE)
#     # email = models.EmailField()
#     # created = models.DateTimeField(default=timezone.now)
#     # approved = models.BooleanField(default=False)
#
#     # def approved(self):
#     #     self.approved = True
#     #     self.save()
#     #
#     # def __str__(self):
#     #     return self.user
#
#     def __str__(self):
#         return self.comment
#
#     @classmethod
#     def get_comments(cls):
#         comments = cls.objects.all()
#         return comments

#
# class Like(models.Model):
#     like = models.IntegerField()
#     image = models.ForeignKey(Image, related_name='liked_by', on_delete=models.CASCADE, null=True)
#     user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return str(self.like)
