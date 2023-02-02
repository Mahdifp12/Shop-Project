from django.contrib import admin
from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_active', 'category']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active',
        'is_delete'
    ]

    list_editable = [
        'is_active',
        'is_delete'
    ]

    list_filter = [
        'is_active',
        'is_delete'
    ]


class ProductTagAdmin(admin.ModelAdmin):
    pass


class ProductBrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
