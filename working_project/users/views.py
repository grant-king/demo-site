from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import VolunteerRequestForm, CollaboratorRequestForm
from django.core.mail import EmailMessage
import os

def contact(request):
    return render(request, 'users/contact.html')

def collaborate(request):
    #if you get a post request, validate that form data
    if request.method == 'POST':
        form = CollaboratorRequestForm(request.POST)
        if form.is_valid():
            form.save()
            to_email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('about')
            subject = 'Your collaboration message to Grant'
            EmailMessage(subject, message, os.environ.get('ALERTS_EMAIL'), [to_email], [os.environ.get('GRANT_EMAIL')]).send()
            messages.success(request, f'Your message has been emailed to Grant. A copy has been sent to you at {to_email}.')
            return redirect('contact')
    else: #otherwise no submit was pressed, display a blank form 
        form = CollaboratorRequestForm()
    
    return render(request, 'users/collaborate.html', {'form': form})

def volunteer_request(request):
    #if you get a post request, validate that form data
    if request.method == 'POST':
        form = VolunteerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            to_email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('description')
            subject = 'Your Volunteer Request for Grant'
            EmailMessage(subject, message, os.environ.get('ALERTS_EMAIL'), [to_email], [os.environ.get('GRANT_EMAIL')]).send()
            messages.success(request, f'Your Volunteer Request has been submitted to Grant. A copy has been sent to you at {to_email}.')
            return redirect('contact')
    else: #otherwise no submit was pressed, display a blank form 
        form = VolunteerRequestForm()
    
    return render(request, 'users/volunteer_request.html', {'form': form})
