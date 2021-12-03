from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Publish'))

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=255, default="Post Title")
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="Comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
