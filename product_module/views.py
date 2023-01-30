from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView

from .models import Product


# Create your views here.

class ProductListView(ListView):
    template_name = "product_module/product_list.html"
    model = Product
    context_object_name = "products"

    # def get_queryset(self):
    #     base_query = super(ProductListView, self).get_queryset()
    #     active_products = base_query.filter(is_active=True)
    #     return active_products


class ProductDetailView(TemplateView):
    template_name = "product_module/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context
