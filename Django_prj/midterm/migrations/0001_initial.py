# Generated by Django 4.2 on 2023-04-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('rank', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='midterm/images/%Y/%m/%d/')),
            ],
        ),
    ]
