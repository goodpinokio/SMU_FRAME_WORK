# Generated by Django 4.1.7 on 2023-05-08 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
