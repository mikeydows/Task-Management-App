from django import forms 
from .models import Profile, Task
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']

class UpdateEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'tasks', 'progress', 'priority'
        ]