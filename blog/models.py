from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class BlogPost(models.Model):

    status_choices = (
        ('pub','Published'),
        ('drft', 'Draft')
    )


    title = models.CharField(max_length = 100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add = True)
    datetime_modified = models.DateTimeField(auto_now = True)
    status = models.CharField(choices= status_choices, max_length = 10)
    author = models.ForeignKey('accounts.CustomUser', on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail' , args=[str(self.id)])


class BlogComment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete= models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add = True)
    
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.author} commented to {self.post}"
    
