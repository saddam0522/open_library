
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('account/', include('accounts.urls')),
    path('bookshelf/', include('BookShelf.urls')),
    path('borrow/', include('borrow.urls')),
    path('catalog/', include('catalog.urls')),
    path('wishlist/', include('wishlist.urls')),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
