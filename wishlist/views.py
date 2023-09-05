from django.shortcuts import render, redirect,get_object_or_404
from .models import Wishlist
from BookShelf.models import BookList
from django.contrib.auth.decorators import login_required


@login_required
def wishlist_view(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    books_in_wishlist = user_wishlist.books.all()

    context = {'books_in_wishlist': books_in_wishlist}
    return render(request, 'wishlist/wishlist.html', context)

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(BookList, pk=book_id)
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    user_wishlist.books.add(book)
    user_wishlist.save()
    return redirect('wishlist', book_id=book_id)

def wishlist(request):
    return render(request,'wishlist/cart.html')