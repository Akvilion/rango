# Generated by Django 3.2.4 on 2021-06-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]