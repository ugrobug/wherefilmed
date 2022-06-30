from django.urls import path
from . import views

from .sitemap import DynamicViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'dynamic': DynamicViewSitemap,
}


urlpatterns = [
    path('', views.movies_home, name='movies_home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('series', views.series_home, name='series_home'), 
    path('create', views.create, name='create'),
    path('genre/<genre_slug>/', views.get_genre, name='genre'),
    path('country/<country_slug>/',views.get_country, name='country'),
    path('<movie_slug>/', views.movies_detail, name='details_view'), 
    path('<int:pk>/update', views.MoviesUpdateView.as_view(), name='movies_update'),
    path('<int:pk>/delete', views.MoviesDeleteView.as_view(), name='movies_delete'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]