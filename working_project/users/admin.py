from django.contrib import admin
from .models import VolunteerRequest, CollaboratorRequest

admin.site.register(VolunteerRequest)
admin.site.register(CollaboratorRequest)
