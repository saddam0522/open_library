from django.db import models
from catalog.models import Category

# Create your models here.

class BookList(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    genre = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    no_of_books_available = models.PositiveIntegerField(default=0)
    last_update =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}-{self.author}-{self.genre}-{self.no_of_books_available}-{self.last_update}"
    
    def search_by_title(cls, query):
        return cls.objects.filter(title__icontains=query)
    