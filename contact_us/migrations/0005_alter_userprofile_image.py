# Generated by Django 4.1.3 on 2023-02-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0004_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='عکس شما'),
        ),
    ]
