# Generated by Django 4.0.6 on 2022-07-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(default='https://assets.asaxiy.uz/product/main_image/desktop//61165331d95f7.jpg'),
        ),
    ]
