from django.contrib import admin
from .models import BlogPost ,BlogComment
# Register your models here.

class PostCommentInLine(admin.TabularInline):
    model = BlogComment
    extra = 2


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    ordering = ['-datetime_modified']
    inlines = [PostCommentInLine]


class PostComment(admin.ModelAdmin):
    list_display = ['author', 'body']
    



admin.site.register(BlogPost, PostAdmin)
admin.site.register(BlogComment, PostComment)
