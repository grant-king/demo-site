from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import VolunteerRequestForm, CollaboratorRequestForm

def contact(request):
    return render(request, 'users/contact.html')

def collaborate(request):
    #if you get a post request, validate that form data
    if request.method == 'POST':
        form = CollaboratorRequestForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your Collaborator Request has been submitted. A copy has been sent to you at {email}.')
            return redirect('contact')
        else:
            pass ## flash message that form needs help
    else: #otherwise no submit was pressed, display a blank form 
        form = CollaboratorRequestForm()
    
    return render(request, 'users/collaborate.html', {'form': form})

def volunteer_request(request):
    #if you get a post request, validate that form data
    if request.method == 'POST':
        form = VolunteerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your Volunteer Request has been submitted. A copy has been sent to you at {email}.')
            return redirect('contact')
        else:
            pass ## flash message that form needs help
    else: #otherwise no submit was pressed, display a blank form 
        form = VolunteerRequestForm()
    
    return render(request, 'users/volunteer_request.html', {'form': form})
