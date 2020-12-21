from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog

#TODO 
#? 1 update i delete dugme u blog detail
#? 2 update olovka
#? 3 ime autora uz blog
#? 4 moji blogovi da se izlistaju
#? 5 paginacija
#? 6 reset passworda i emaila


def home(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, 'blog/home.html', context) # u template-u filter datuma, prikazati authora   

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted'] # opadajuce po vremenu


class MyBlogsListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted'] 

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user)

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'image', 'content']
    
    def form_valid(self, form):  # postavi da je autor bloga ulogovani user pa onda validira
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'image', 'content']
    
    def form_valid(self, form):  
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object() # blog koji update-ujem
        if self.request.user == blog.author:
            return True
        return False
    
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False