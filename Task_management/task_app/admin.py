from django.contrib import admin
from .models import Task, User   # but ONLY if User is in models.py

admin.site.register(Task)


