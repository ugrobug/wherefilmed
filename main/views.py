from django.shortcuts import render
from movies.models import Movies 

def index(request):
    movies = Movies.objects.order_by('-date').filter(type_item='movie')[:4]
    clips = Movies.objects.order_by('-date').filter(type_item='clip')[:4]
    series = Movies.objects.order_by('-date').filter(type_item='series')[:4]
    return render(request, 'main/index.html', {"movies":movies, "clips":clips, "series":series})
    

def about(request):
    return render(request, 'main/about.html')


