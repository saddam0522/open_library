from django.shortcuts import render, redirect, get_object_or_404
from BookShelf.models import BookList
from .models import Borrowing
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(BookList, pk=book_id)

    if book.available_copies > 0:
        # Create a borrowing record and reduce available copies by 1
        borrowing = Borrowing(user=request.user, book=book)
        borrowing.save()

        book.available_copies -= 1
        book.save()

        messages.success(request, f"You have successfully borrowed '{book.title}'.")
    else:
        messages.error(request, f"'{book.title}' is not available for borrowing.")

    return redirect('book_detail', book_id=book_id)

def order_cmpleted(request):
    return render(request,'borrow/order_complete.html')