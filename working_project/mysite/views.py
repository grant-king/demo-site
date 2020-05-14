from django.shortcuts import render
from .models import Project

project_list = [
    {
        'title': 'Project 1',
        'description': 'Project Description'
    },
    {
        'title': 'Project 2',
        'description': 'Project 2 Description'
    },
    {
        'title': 'Project 3',
        'description': 'Project 3 Description'
    },
    {
        'title': 'Project 4',
        'description': 'Project Description'
    },
    {
        'title': 'Project 5',
        'description': 'Project 2 Description'
    },
    {
        'title': 'Project 6',
        'description': 'Project 3 Description'
    },
    {
        'title': 'Project 7',
        'description': 'Project Description'
    },
    {
        'title': 'Project 8',
        'description': 'Project 2 Description'
    },
]

def home(request):
    return render(request, 'mysite/home.html')

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'mysite/projects.html', context)

