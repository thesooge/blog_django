from django import forms
from .models import BlogPost, BlogComment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'status', 'author']

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['body']
        
                 