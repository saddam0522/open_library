# Generated by Django 4.2.4 on 2023-09-04 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookShelf', '0002_booklist_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booklist',
            name='id',
        ),
        migrations.AddField(
            model_name='booklist',
            name='book_id',
            field=models.IntegerField(default='book', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]