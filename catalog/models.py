from django.db import models

# Create your models here.
 

class Category(models.Model):
    genre = models.CharField(max_length=20,unique=True)
    image = models.ImageField(upload_to='photos/catalog')
    def __str__(self):
        return self.genre