from django.contrib import admin
from .models import BlogPost
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    ordering = ['-datetime_modified']

admin.site.register(BlogPost, PostAdmin)