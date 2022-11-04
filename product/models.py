from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.TextField()
    image = models.ImageField()



class Product(models.Model):
    title = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.ForeignKey('Category',on_delete= models.CASCADE)
    trending = models.BooleanField(default=False)