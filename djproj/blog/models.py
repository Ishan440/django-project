from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length =100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # Each user is unique but posts are not so we set author as the key
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if user is deleted, delete all their posts

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        # redirect actually leads you to the route whereas reverse returns the url as a string.
