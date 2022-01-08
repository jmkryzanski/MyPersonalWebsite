from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=10000, default="hello world")

    def __str__(self):
        return str(self.user)