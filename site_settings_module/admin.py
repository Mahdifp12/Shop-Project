from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


# Todo : I must add a new class for SliderAdmin ..!

admin.site.register(models.SiteSettings)
admin.site.register(models.FooterLinksBox)
admin.site.register(models.FooterLink, FooterLinkAdmin)
admin.site.register(models.Slider)
