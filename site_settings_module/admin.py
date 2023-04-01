from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SliderAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "url"]
    list_editable = ["is_active", "url"]


admin.site.register(models.SiteSettings)
admin.site.register(models.FooterLinksBox)
admin.site.register(models.FooterLink, FooterLinkAdmin)
admin.site.register(models.Slider, SliderAdmin)
