from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('volunteer_request/', views.volunteer_request, name='volunteer_request'),
]
