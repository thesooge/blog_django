from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse
from django.views import generic
from .models import BlogPost
from .forms import AddPostForm
# Create your views here.

class BlogPostListedView(generic.ListView):
    template_name = 'blog/blog-post.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return BlogPost.objects.filter(status= 'pub').order_by('datetime_modified')
    
class BlogPostDetailView(generic.DetailView):
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
    model = BlogPost


class DeletPost(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/post-delete.html'
    # or
    # success_url = reverse_lazy('home)
    def get_success_url(self) -> str:
        return reverse('home')
    
class UpdatePost(generic.UpdateView):
    model = BlogPost
    template_name = 'blog/post-update.html'
    context_object_name = 'post'
    form_class = AddPostForm

class AddPost(generic.CreateView):
    model = BlogPost
    template_name = 'blog/addpost.html'
    context_object_name = 'post'
    form_class = AddPostForm    

