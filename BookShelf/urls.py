from django.urls import path,include
from . import views

urlpatterns = [
    path('products/',views.products,name='product'),
    path('product_by_category/<str:category_genre>/',views.search_results,name='product_by_category'),
    path('store/',views.store,name='store'),
    path('catagory/',views.store,name='store'),
    path('search/',views.search_book,name='search_book'),
    path('book_details/',views.book_details,name='book_details'),
]
