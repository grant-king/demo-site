from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView, ProjectTagListView

urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('projects/', ProjectListView.as_view(), name='mysite-projects'),
    path('projects/<tag_name>/', ProjectTagListView.as_view(), name='projects-category'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
