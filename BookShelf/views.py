from django.shortcuts import render,get_object_or_404
from .models import BookList
from catalog.models import Category
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q
from .forms import BookSearchForm
# Create your views here.



def products(request):
    return render(request,'BookShelf/product-detail.html')

def search_results(request):
    return render(request,'BookShelf/search-result.html')

def store(request):
    book = BookList.objects.all()
    categories = Category.objects.all()
    page = request.GET.get('page')
    paginator = Paginator( book, 3)
    page_product = paginator.get_page(page)
    for i in page_product:
        print(i)
    
    context = {'book':page_product, 'categories':categories}
    return render(request,'BookShelf/store.html', context)


def book_details(request):
    return render(request, 'store/product_details.html')



def search_book(request):
    title = request.POST.get('query')
    if title:
        books = BookList.objects.filter(title__icontains=title)
    else:
        books = BookList.objects.all()
        
    return render(request, 'BookShelf/search-result.html', {'books':books, 'query':title})    
    
    
class BookListView(ListView):
    model = BookList
    template_name = 'BookShelf/store.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query')
        
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = BookSearchForm(self.request.GET)
        return context
