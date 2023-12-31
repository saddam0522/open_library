# Generated by Django 4.2.4 on 2023-09-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='photos/catalog')),
            ],
        ),
    ]
