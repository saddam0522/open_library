from django.shortcuts import render
from BookShelf.models import BookList
from catalog.models import Category
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    book = BookList.objects.all()
    categories = Category.objects.all()
    page = request.GET.get('page')
    paginator = Paginator( book, 3)
    page_product = paginator.get_page(page)
    for i in page_product:
        print(i)
    
    context = {'book':page_product, 'categories':categories}
    return render(request,'BookShelf/store.html', context)


