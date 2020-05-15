from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import VolunteerRequest, CollaboratorRequest

class VolunteerRequestForm(forms.ModelForm):
    email = forms.EmailField()
    description = forms.CharField()
    class Meta:
        model = VolunteerRequest
        fields = ['email', 'description']

class CollaboratorRequestForm(forms.ModelForm):
    email = forms.EmailField()
    about = forms.CharField()
    class Meta:
        model = CollaboratorRequest
        fields = ['email', 'about']

