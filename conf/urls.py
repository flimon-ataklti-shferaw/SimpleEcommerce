from django.contrib import admin
from django.urls import path

from products.views import ProductListView, ProductDetailView

from carts.views import cart_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart_view, name='cart'),
    path('', ProductListView.as_view(), name='productlist'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='productdetail'),
]
