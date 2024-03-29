from django.db import models


# Create your models here.

class SiteSettings(models.Model):
    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")
    site_name = models.CharField(max_length=250, verbose_name="نام سایت")
    address = models.CharField(max_length=250, verbose_name="آدرس")
    phone = models.CharField(max_length=250, null=True, verbose_name="شماره تلفن")
    fax = models.CharField(max_length=250, null=True, verbose_name="فکس")
    email = models.CharField(max_length=250, null=True, verbose_name="ایمیل")
    copy_right_text = models.TextField(verbose_name="متن کپی رایت")
    site_logo = models.ImageField(upload_to="images/site_settings/", verbose_name="لوگو سایت")
    site_url = models.CharField(max_length=250, verbose_name="دامنه سایت")
    about_us = models.TextField(verbose_name="درباره ما")
    git_hub_url = models.URLField(verbose_name="آدرس گیت هاب", max_length=250, null=True)

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات"

    def __str__(self):
        return self.site_name


class FooterLinksBox(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")

    class Meta:
        verbose_name = "دسته بندی لینک های فوتر"
        verbose_name_plural = "دسته بندی های لینک های فوتر"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان")
    url = models.URLField(max_length=600, verbose_name="لینک")
    footer_link_box = models.ForeignKey(to=FooterLinksBox, verbose_name="دسته بندی", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک های فوتر"

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان", )
    description = models.TextField(verbose_name="توضیحات اسلایدر")
    url = models.URLField(max_length=500, verbose_name="لینک")
    url_title = models.CharField(max_length=150, verbose_name="َعنوان لینک")
    image = models.ImageField(verbose_name="تصویر اسلایدر", upload_to="images/slider/")
    is_active = models.BooleanField(verbose_name="فعال/غیرفعال", default=True)

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"

    def __str__(self):
        return self.title
