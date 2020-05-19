from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import VolunteerRequest, CollaboratorRequest

class VolunteerRequestForm(forms.ModelForm):
    email = forms.EmailField(label='Your Email')
    description = forms.CharField(label='Project Description', help_text='Briefly describe your project and goals.')

    class Meta:
        model = VolunteerRequest
        fields = ['email', 'description']

class CollaboratorRequestForm(forms.ModelForm):
    email = forms.EmailField(label='Your Email')
    about = forms.CharField(label='About You', help_text='Please tell me about yourself. What do you do? What are your areas of interest?')

    class Meta:
        model = CollaboratorRequest
        fields = ['email', 'about']

