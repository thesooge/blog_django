
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BlogPostListedView.as_view(), name='home'),
    path('post_detail/<int:pk>', views.BlogPostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete', views.DeletPost.as_view(), name='delete'),
    path('<int:pk>/update', views.UpdatePost.as_view(), name='update_post'),
    path('addpost/', views.AddPost.as_view(), name='addpost'),
    path('addcomment/<int:pk>', views.ProductComment.as_view(), name='addcomment'),
]