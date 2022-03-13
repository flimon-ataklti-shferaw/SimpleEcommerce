from django.contrib import admin
from django.urls import path

from products.views import ProductListView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='productlist'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='productdetail')
]
