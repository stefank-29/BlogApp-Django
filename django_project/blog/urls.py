from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, MyBlogsListView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('blogs/', BlogListView.as_view(), name='blog-blogs'),
    path('myblogs/', MyBlogsListView.as_view(), name='blog-myblogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('add/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('reviews/<int:pk>/', views.addReview, name='blog-comment'),

]

