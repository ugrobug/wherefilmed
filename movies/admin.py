from django.contrib import admin
from .models import Movies, Locations, Country , Genre, LocationsGalleryReal, LocationsGalleryMovie

save_on_top = True

class GalleryInline(admin.TabularInline):
    fk_name = 'location'
    model = LocationsGalleryReal
    
class GalleryInline2(admin.TabularInline):
    fk_name = 'location'
    model = LocationsGalleryMovie

@admin.register(Locations)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, GalleryInline2]
    raw_id_fields = ('movie',)
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("genre_name",)}

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("country_name",)}

    
@admin.register(Movies)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title","year")}
    search_fields = ['title']
    
    
admin.site.site_title = 'Where Filmed Admin'
admin.site.site_header = 'Where Filmed Admin'
