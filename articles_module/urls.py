from django.urls import path
from . import views
urlpatterns = [
    path('', views.ArticleListView.as_view(), name="article-list"),
    path('cat/<str:category>', views.ArticleListView.as_view(), name="articles-by-category-list"),
    path('<int:pk>', views.ArticleDetailView.as_view(), name="article-detail"),
    path('add-article-comment', views.add_article_comment, name="add-article-comment")
]