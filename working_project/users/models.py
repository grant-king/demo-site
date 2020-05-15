from django.db import models
from django.contrib.auth.models import User

class VolunteerRequest(models.Model):
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return f'{self.email}'


class CollaboratorRequest(models.Model):
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return f'{self.email}'

