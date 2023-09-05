from django.contrib import admin
from .models import BookList
# Register your models here.


# class BookListAdmin(admin.ModelAdmin):
#     list_display=['tittle','author','genre','no_of_books_available','last_update',]
    
# admin.site.register(BookList, BookListAdmin)


class BookListAdmin(admin.ModelAdmin):
    list_display = ['title','author','genre','no_of_books_available','last_update',]
    
admin.site.register(BookList,BookListAdmin)

# admin.site.register(BookList)