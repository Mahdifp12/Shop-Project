from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory, ProductBrand


class ProductListView(ListView):
    template_name = "product_module/product_list.html"
    model = Product
    context_object_name = "products"
    ordering = ['-price']
    paginate_by = 6

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        query2 = super(ProductListView, self).get_queryset()
        query = query.filter(is_active=True)
        query2 = query.filter(is_active=True)
        category_name = self.kwargs.get("category")
        brand_name = self.kwargs.get("brand")
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        if brand_name is not None:
            query2 = query2.filter(brand__url_title__iexact=brand_name)
            return query2

        return query


class ProductDetailView(DetailView):
    template_name = "product_module/product_detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        self_product = self.object
        request = self.request
        product_favorite = request.session.get("product_favorite")
        is_favorite = product_favorite == self_product.id
        context["is_favorite"] = is_favorite
        return context


class ProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product.id
        return redirect(product.get_absolute_url())


def product_categories_components(request: HttpRequest):
    product_categories = ProductCategory.objects.prefetch_related("productcategory_set") \
        .filter(is_active=True, is_delete=False, parent_id=None)

    context = {
        "product_categories": product_categories
    }

    return render(request, template_name="product_module/components/product_categories_component.html", context=context)


def product_brands_components(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True)

    context = {
        "product_brands": product_brands
    }

    return render(request, "product_module/components/product_brands_component.html", context)
