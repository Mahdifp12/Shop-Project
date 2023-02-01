from django.contrib import admin
from . import models


# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'title',
        'created_date'
    ]


admin.site.register(models.ContactUs, ContactUsAdmin)
