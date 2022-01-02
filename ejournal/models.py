from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default='Article Title')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)


