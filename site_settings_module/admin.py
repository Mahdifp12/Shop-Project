from django.contrib import admin
from . import models


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


admin.site.register(models.SiteSettings)
admin.site.register(models.FooterLinksBox)
admin.site.register(models.FooterLink, FooterLinkAdmin)
