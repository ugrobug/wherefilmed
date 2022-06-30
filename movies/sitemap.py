from django.contrib.sitemaps import Sitemap
from .models import Movies
from django.shortcuts import reverse

class DynamicViewSitemap(Sitemap):

    def items(self):
        return Movies.objects.all()

    def location(self, item):
        return f'/movies/{item.slug}/'
    