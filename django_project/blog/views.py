from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog


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

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']
    
    def form_valid(self, form):  # postavi da je autor bloga ulogovani user pa onda validira
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    
    def form_valid(self, form):  
        form.instance.author = self.request.user
        return super().form_valid(form)