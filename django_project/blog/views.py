from django.shortcuts import render
from django.http import HttpResponse

def main_home(request):
    return render(request, 'blog/home.html')

def blog_home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about-us.html')