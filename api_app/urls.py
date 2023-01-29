from django.urls import path
from . import views

urlpatterns = [
    path('api', views.ProductApiList.as_view())
]