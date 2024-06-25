from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import (BlogPostListView, BlogPostCreateView, BlogPostDeleteView, BlogPostDetailView,
                         BlogPostUpdateView, blog_main)

app_name = BlogsConfig.name
urlpatterns = [
    path('', blog_main, name='blog_main_page'),
    path('blog_list/', BlogPostListView.as_view(), name='blog_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post'),
    path('post/create', BlogPostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', BlogPostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post_delete')
]
