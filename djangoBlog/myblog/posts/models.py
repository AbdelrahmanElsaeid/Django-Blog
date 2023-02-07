from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_author")
    title = models.CharField(max_length=100, help_text = 'Must be unique',error_messages = {
        "unique" : 'This title is not unique please try again ',
        "blank" : 'This field is not full please try again'})
    content = models.TextField(max_length=10000)
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts/')
    slug = models.SlugField(null=True,blank=True)

    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    



    def __str__(self) -> str:
        return self.title


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)
    