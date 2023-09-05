from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.wishlist,name='wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist_view'),
    path('add-to-wishlist/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),

]