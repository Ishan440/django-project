from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # Each user is unique but posts are not so we set author as the key
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if user is deleted, delete all their posts

    def __str__(self):
        return self.title
