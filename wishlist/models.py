
from django.contrib.auth.models import User
from django.db import models
from BookShelf.models import BookList 

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(BookList)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
