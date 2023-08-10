from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account_app.models import User

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")
    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / حذف نشده")
    parent = models.ForeignKey('ProductCategory', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')

    def __str__(self):
        return f'({self.title}) - ({self.url_title})'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="عنوان برند")
    url_title = models.CharField(max_length=300, db_index=True, null=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    image = models.ImageField(verbose_name="عکس", upload_to="images/products", null=True, blank=True)
    category = models.ManyToManyField(ProductCategory,
                                      related_name='product_categories',
                                      verbose_name='دسته بندی ها',
                                      )
    price = models.IntegerField(verbose_name="قیمت")
    short_description = models.CharField(max_length=400, db_index=True, null=True, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name="توضیحات اصلی", db_index=True)
    is_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name="برند", null=True, blank=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name="عنوان در url")
    is_delete = models.BooleanField(default=False, verbose_name="حذف شده / حذف نشده")

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}  ({self.price})"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان تگ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_tags", verbose_name="محصول")

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    
    
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return f"{self.user} - {self.product} ({self.quantity})"