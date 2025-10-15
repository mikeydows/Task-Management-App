from django.db import models
from django.contrib.auth.models import User   # built-in User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    tasks = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_image = models.ImageField(upload_to = 'profile_pics/', default = 'default.jpg')

    def __str__(self):
        return self.username