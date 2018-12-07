from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def main_home(request):
    return render(request, 'blog/home.html')

def blog_home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about-us.html')

def explore(request):
    return render(request, 'blog/explore.html')