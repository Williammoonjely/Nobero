from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.TextField()
    images = models.ImageField(upload_to='Categories')

    def __str__(self):
        return self.title
