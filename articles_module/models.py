from django.db import models


# Create your models here.

class ArticleCategory(models.Model):
    parent = models.ForeignKey("ArticleCategory", null=True, on_delete=models.CASCADE, verbose_name="دسته بندی والد")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    url_title = models.CharField(max_length=200, unique=True, verbose_name="عنوان url دسته بندی")
    is_active = models.BooleanField(verbose_name="فعال / غیر فعال", default=True)

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی های مقاله"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name="عنوان در URL")
    image = models.ImageField(upload_to="images/articles/", verbose_name="تصویر مقاله")
    short_description = models.TextField(verbose_name="توضیحات کوتاه")
    text = models.TextField(verbose_name="متن مقاله")
    is_active = models.BooleanField(default=True, verbose_name="فعال / غیرفعال")
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name="دسته بندی ها", )

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
