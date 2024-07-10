from django import forms
from .models import BlogPost

class AddPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'status', 'author']