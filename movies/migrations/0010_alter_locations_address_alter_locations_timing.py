# Generated by Django 4.0.4 on 2022-06-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_remove_movies_genre_movies_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='address',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Location address'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='timing',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Time in movie'),
        ),
    ]
