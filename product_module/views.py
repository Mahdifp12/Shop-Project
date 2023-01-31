from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    template_name = "product_module/product_list.html"
    model = Product
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "product_module/product_detail.html"
    model = Product
