from django.db import models
from django.contrib.auth.models import User

class Project(models.Model): #portfolio item data structure
    title = models.CharField(max_length=100)
    description = models.TextField()
    collaborators = models.ManyToManyField(User)

    def __str__(self):
        return self.title
