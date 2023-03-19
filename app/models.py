from django.db import models
from django.utils import timezone

# built in user, for our Authors
from django.contrib.auth.models import User

# Creating posts for website
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Makes it to where when post it shows the date posted, but when updated the date updates to the day it updates
    date_posted = models.DateTimeField(default=timezone.now)
    # ForeignKey OnetoMany, we pass in the User related table. Association.
    # If a User gets deleted, then we want to delete their post as well.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
