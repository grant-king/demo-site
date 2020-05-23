from django.shortcuts import render, get_object_or_404
from .models import Project, CategoryTag
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

class ProjectTagListView(ListView):
    model = Project
    template_name = 'mysite/projects_tag.html'
    context_object_name = 'projects'
    ordering = ['title']
    paginate_by = 8

    def get_queryset(self):
        tag = get_object_or_404(CategoryTag, name=self.kwargs.get('tag_name'))
        return Project.objects.filter(tags=tag)


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'

