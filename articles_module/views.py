from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Article


# Create your views here.

class ArticlesView(ListView):
    model = Article
    paginate_by = 4
    template_name = "articles_module/articles_page.html"
