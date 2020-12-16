from django.shortcuts import render
from .models import Blog

def home(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, 'blog/home.html', context) # u template-u filter datuma, prikazati authora