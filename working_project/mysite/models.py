from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class CategoryTag(models.Model):
    name = models.CharField(max_length=25)
    display_title = models.CharField(max_length=25)

    def __str__(self):
        return self.display_title


class Project(models.Model): #portfolio item data structure
    image = models.ImageField(default='default.png', upload_to='project_pics')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    summary = models.TextField(max_length=250)
    description = models.TextField()
    #collaborators = models.ManyToManyField(User)
    tags = models.ManyToManyField(CategoryTag)
    app_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

#    def save(self, *args, **kwargs):
#        MAX_SIZE = (1080, 1920) #height, width
#
#        super().save(*args, **kwargs)
#        img = Image.open(self.image.path)
#
#        if img.height > MAX_SIZE[0] or img.width > MAX_SIZE[1]:
#            size = (img.height, img.width)
#            resize_ratio = min(MAX_SIZE[0] / size[0], MAX_SIZE[1] / size[1])
#            new_size = [size[0] * resize_ratio, size[1] * resize_ratio]
#            img.thumbnail(new_size)
#            img.save(self.image.path)
