from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # filter_horizontal =('tags',)
# Register your models here.

admin.site.register(Post,PostAdmin)
# admin.site.register(tags)
