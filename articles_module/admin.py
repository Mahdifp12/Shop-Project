from django.contrib import admin
from . import models


# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'parent',
        'url_title',
        'is_active'
    ]
    list_editable = [
        'parent',
        'is_active',
        'url_title'
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'slug'
    ]

    list_editable = [
        'is_active',
        'slug'
    ]


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
