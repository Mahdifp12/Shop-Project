from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductApiList.as_view(), name="product-api-list"),
    path('<int:pk>', views.product_api_view_detail, name="product-api-detail")
]