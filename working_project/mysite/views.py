from django.shortcuts import render
from .models import Project
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'mysite/home.html')

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'mysite/projects.html', context)


class ProjectListView(ListView):
    model = Project
    template_name = 'mysite/projects.html'
    context_object_name = 'projects'
    ordering = ['title']
    paginate_by = 8


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'

