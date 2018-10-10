# from django.contrib.auth.models import User
# from django.db import models
# import datetime as dt
# from tinymce.models import HTMLField
#
#
# # Create your models here.
# class Subscribers(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile = models.ImageField(null=True, blank=True)
#     bio = models.TextField()
#     # dob = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return 'Profile of user {}'.format(self.username)
#
# #
# # class Image(models.Model):
# #     post = models.CharField(max_length=60)
# #     caption = models.TextField()
# #     post_date = models.DateTimeField(auto_now_add=True)
# #     image = models.ImageField(upload_to = 'post/')
# #     profile = models.ForeignKey(User,on_delete=models.CASCADE)
# #
# #     def __str__(self):
# #         return self.name
# #
# #     @classmethod
# #     def all_posts(cls):
# #         image = cls.objects.order_by('post_date')
# #         return image
# #
# #     @classmethod
# #     def get_image(cls, id):
# #         image = cls.objects.get(id=id)
# #         return image
# #
# #
# #     @classmethod
# #     def search_by_image(cls,search_term):
# #         pictures = cls.objects.filter(profile__profile__icontains=search_term)
# #         return pictures
