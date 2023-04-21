from django.urls import path
from . import views
urlpatterns = [
    path('', views.ArticlesView.as_view(), name="article-list"),
    path('cat/<str:category>', views.ArticlesView.as_view(), name="articles-by-category-list")
]