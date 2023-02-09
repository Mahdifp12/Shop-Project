from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    template_name = "product_module/product_list.html"
    model = Product
    context_object_name = "products"


class ProductDetailView(DetailView):
    template_name = "product_module/product_detail.html"
    model = Product


class ProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product.id
        return redirect(product.get_absolute_url())
