from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name="کد فعالسازی ایمیل")
    avatar = models.ImageField(upload_to="images/users_avatar", verbose_name="تصویر آواتار", null=True, blank=True)
    about_user = models.TextField(null=True, blank=True, verbose_name="درباره شخص")
    address = models.TextField(null=True, blank=True, verbose_name="آدرس")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()

        return self.email
