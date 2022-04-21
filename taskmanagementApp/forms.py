from django import forms
from .models import TaskDb

class Taskform(forms.ModelForm):
    class Meta:
        model = TaskDb
        fields = ['task','priority']
