from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name="کد فعالسازی ایمیل")
    avatar = models.CharField(max_length=20, verbose_name="تصویر آواتار", null=True, blank=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

    def __str__(self):
        return self.get_full_name()
