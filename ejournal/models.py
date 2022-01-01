from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)