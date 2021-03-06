# Generated by Django 4.0.4 on 2022-06-03 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_locationsgallery_image_locationsgallery_movie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationsGalleryMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_image', models.ImageField(blank=True, null=True, upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='LocationsGalleryReal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_image', models.ImageField(blank=True, null=True, upload_to='gallery')),
            ],
        ),
        migrations.RemoveField(
            model_name='locations',
            name='movie_img',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='real_img',
        ),
        migrations.DeleteModel(
            name='LocationsGallery',
        ),
        migrations.AddField(
            model_name='locationsgalleryreal',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='movies.locations'),
        ),
        migrations.AddField(
            model_name='locationsgallerymovie',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagesM', to='movies.locations'),
        ),
    ]
