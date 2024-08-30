from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, reverse,get_object_or_404
from django.views import generic
from .models import BlogPost, BlogComment
from .forms import AddPostForm, CommentPostForm
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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentPostForm()
        return context

class ProductComment(generic.CreateView):
    model = BlogComment
    form_class = CommentPostForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        obj = form.save(commit=False)
        obj.author = self.request.user
        post_id = int(self.kwargs['pk'])
        obj.post = get_object_or_404(BlogPost, id= post_id)

        return super().form_valid(form)



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

