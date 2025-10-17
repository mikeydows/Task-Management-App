from django.db import models
from django.contrib.auth.models import User   # built-in User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    tasks = models.TextField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(auto_now_add = True, null = True)
    progress = models.IntegerField(default = 0)
    priority = models.CharField(
        max_length=20, 
        choices = [
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
        ],
        default="Medium"
    )

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_image = models.ImageField(upload_to = 'profile_pics/', default = 'user.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'