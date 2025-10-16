from django import forms 
from .models import Profile, Task

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'progress', 'completed', 'priority'
        ]