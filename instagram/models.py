from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# from django.db.models.signals import post_save
# from django.utils import timezone

class Image(models.Model):
    user = models.ForeignKey(User, related_name="editor", on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='post/')
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

    # @classmethod
    # def search_by_category(cls,search_term):
    #     pictures = cls.objects.filter(category__category__icontains=search_term)
    #     return pictures

class Comments(models.Model):
    content = models.CharField(max_length = 300)



    # @classmethod
    # def search_by_category(cls,search_term):
    #     pictures = cls.objects.filter(category__category__icontains=search_term)
    #     return pictures
    #
    # @classmethod
    # def search_by_location(cls,search):
    #     images = cls.objects.filter(location__location__icontains=search)
    #     return images
