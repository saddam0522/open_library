
from django.db import models
from BookShelf.models import BookList

class Borrowing(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(BookList, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} borrowed {self.book} on {self.borrow_date}"
