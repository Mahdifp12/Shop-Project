# Generated by Django 4.1.3 on 2023-02-02 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_module.product', verbose_name='محصول'),
        ),
    ]