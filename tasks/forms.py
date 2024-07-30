from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add your new task'}))

    class Meta:
        model = Task
        fields = '__all__'

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
