from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/add/', BlogCreateView.as_view(), name='blog-create'),

]
