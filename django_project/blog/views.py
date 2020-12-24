from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog
from .forms import CommentForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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

    

class MyBlogsListView(LoginRequiredMixin,  ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted'] 
    paginate_by = 3

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user).order_by('-date_posted')

class BlogDetailView(FormView,DetailView):
    model = Blog
    form_class = CommentForm
    fields = ['comment']
    

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

@login_required
def addReview(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() :
            obj = form.save(commit=False)
            obj.user = request.user
            obj.blog = Blog.objects.filter(pk=pk).first()
            obj.save()
            messages.success(request, 'Your comment has been submited.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'), form)
            
        

    

    