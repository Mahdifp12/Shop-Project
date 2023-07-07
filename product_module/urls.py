from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<str:category>', views.ProductListView.as_view(), name="products-by-category-list"),
    path('bra/<str:brand>', views.ProductListView.as_view(), name='product-by-brand-list'),
    path('product-favorite', views.ProductFavorite.as_view(), name='product-favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
