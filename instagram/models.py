from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile/',null=True, blank=True)
    bio = models.TextField()


class Post(models.Model):
    title= models.CharField(max_length=300, unique=True)
    url= models.SlugField(max_length=300)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    author= models.ForeignKey(User)
    post = models.ImageField(upload_to='post/',null=True, blank=True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Preference(models.Model):
    user= models.ForeignKey(User)
    post= models.ForeignKey(Post)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)


    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")
