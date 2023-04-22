from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from .models import Article, ArticleCategory


class ArticleListView(ListView):
    model = Article
    paginate_by = 4
    template_name = "articles_module/articles_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        category_name = self.kwargs.get("category")
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)

        return query


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)

    context = {
        'article_main_categories': article_main_categories,
    }

    return render(request, "articles_module/components/article_categories_component.html", context)
