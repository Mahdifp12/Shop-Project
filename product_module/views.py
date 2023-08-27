from django.contrib import messages
from django.http import HttpRequest, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import QuantityForm
from .models import Product, ProductCategory, ProductBrand, ShoppingCart


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


class ShoppingCartView(View):
    template_name = "product_module/shopping_cart_page.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        user = request.user
        cart_items = ShoppingCart.objects.filter(user=user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }

        return render(request, self.template_name, context)


class AddShoppingCart(View):
    def get(self, request: HttpRequest):
        form = QuantityForm()

        context = {
            'form': form
        }

        return render(request, "product_module/product_detail.html", context)

    def post(self, request: HttpRequest):
        product_id = request.POST.get("product_id")
        if product_id:
            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                return HttpResponseBadRequest("محصول یافت نشد")

            user = request.user
            # quantity = form.cleaned_data['quantity']
            try:
                cart_item = ShoppingCart.objects.get(user=user, product=product)
            except ShoppingCart.DoesNotExist:
                cart_item = ShoppingCart(user=user, product=product)
                cart_item.save()
            else:
                cart_item.quantity += 1
                cart_item.save()
        else:
            return HttpResponseBadRequest("ورودی مجاز نیست")

        messages.success(request, "محصول با موفقیت به سبد خرید شما اضافه شد.")

        return redirect(reverse("shopping-cart-view"))


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
