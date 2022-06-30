from django.urls import path
from . import views
import movies.views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('series', movies.views.series_home, name='series'),
    path('clips', movies.views.clips_home, name='clips')
]