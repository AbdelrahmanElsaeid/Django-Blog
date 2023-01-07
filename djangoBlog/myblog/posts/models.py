from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_author")
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts/')