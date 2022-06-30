from django.db import models
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 

#Класс для общей информации о фильмах, сериалах, клипах
class Movies(models.Model):
    #Список типов 
    type_item_choises = (('movie','Movie'),('series','Series'),('clip','Clip'))
    #Поля базы
    title = models.CharField("Title", max_length=100, db_index=True)
    slug = models.SlugField( null=True, unique=True, db_index=True, verbose_name="URL")
    original_lang_title = models.CharField('Original Title', max_length=100, db_index=True)
    mdb_link = models.URLField ('Link to foreign DB', unique=True)
    #Два поля ниже содержат проверку на год элемента, от 1895(Дата первого фильма) до текущий год + 2,
    year = models.IntegerField('Year', validators=[MinValueValidator(1894), MaxValueValidator(datetime.datetime.now().year+2)], db_index=True)
    description = models.TextField("Shooting description")
    date = models.DateTimeField('Date')
    type_item =  models.CharField('Type off item', max_length=100, choices = type_item_choises)
    poster = models.ImageField('Poster', upload_to='gallery/%Y-%m-%d/')
    #Поля базы из других таблиц
    country = models.ManyToManyField('Country', blank=True, null=True)
    genre = models.ManyToManyField('Genre',  blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/movies/{self.slug}'    
    
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        
class Locations (models.Model):
    movie = models.ForeignKey('Movies', on_delete = models.CASCADE, blank=True, null=True)
    title_location = models.CharField('Locations Title', max_length=100, db_index=True)
    scene_description = models.TextField('Scene', db_index=True)
    movie_spot = models.TextField('Spot')
    address = models.CharField('Location address', max_length=100, db_index=True, blank=True, null=True)
    map_link = models.URLField('Map Link')
    gps_coordinate = models.CharField('GPS', max_length=100)
    timing = models.CharField('Time in movie', max_length=100, blank=True, null=True)
    
    
    def get_absolute_url(self):
        return reverse("genre", kwargs={"movie_id": self.pk})
    
    def __str__(self):
        return self.title_location
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    
    
class Country (models.Model):
    country_name = models.CharField('Country', max_length=30, unique=True, db_index=True)
    country_description = models.TextField('Country Description', blank=True, null=True)
    slug = models.SlugField( null=True, unique=True, db_index=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return f'/movies/country/{self.slug}' 
   
    
    def __str__(self):
        return self.country_name
    
    class Meta:
        verbose_name = 'сountry'
        verbose_name_plural = 'countries'
    
class Genre (models.Model):
    genre_name = models.CharField('Genre', max_length=30, unique=True, db_index=True)
    genre_description = models.TextField('Genre description', blank=True, null=True)
    slug = models.SlugField( null=True, unique=True, db_index=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return f'/movies/genre/{self.slug}' 
     
    def __str__(self):
        return self.genre_name
    
class LocationsGalleryReal(models.Model):
     real_image = models.ImageField(upload_to='gallery/%Y-%m-%d/', blank=True, null=True)
     location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='images')
     
class LocationsGalleryMovie(models.Model):
     movie_image = models.ImageField(upload_to='gallery/%Y-%m-%d/', blank=True, null=True)
     location = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='imagesM')
     

