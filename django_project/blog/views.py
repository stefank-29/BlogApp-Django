from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog

#TODO 
#? 3 sort by date
#? 4 front validation za registraciju i login



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
    paginate_by = 3


class MyBlogsListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted'] 
    paginate_by = 3

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user).order_by('-date_posted')

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