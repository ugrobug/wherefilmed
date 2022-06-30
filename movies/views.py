from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Movies, Locations, Genre, Country
from .forms import MoviesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def movies_home(request):
    movies = Movies.objects.order_by('-date').filter(type_item='movie')
    return render(request, 'movies/movies_home.html', {"movies":movies})

def series_home(request):
    movies = Movies.objects.order_by('-date').filter(type_item='series')
    return render(request, 'movies/series_home.html', {"series":movies})

def clips_home(request):
    movies = Movies.objects.order_by('-date').filter(type_item='clip')
    return render(request, 'movies/clips_home.html', {"clips":movies})
    
def get_genre(request, genre_slug):
    genres = Genre.objects.all()
    genre = Genre.objects.get(slug=genre_slug)
    movies = Movies.objects.filter(genre=genre.id)
    return render(request, 'movies/genre.html', {"movies":movies, 'genres':genres, 'genre':genre})

def get_country(request, country_slug):
    countries = Country.objects.all()
    country = Country.objects.get(slug=country_slug)
    movies = Movies.objects.filter(country=country.id)
    return render(request, 'movies/country.html', {"movies":movies, 'countries':countries, 'country':country})
   
def movies_detail(request, movie_slug):
    movie = Movies.objects.get(slug = movie_slug)
    locations = Locations.objects.filter(movie = movie.id)
    return render(request, 'movies/details_view.html', {'movie':movie, 'locations':locations})
       
class MoviesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/'
    model = Movies
    template_name = 'movies/create.html'
    form_class = MoviesForm
    
class MoviesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/'
    model = Movies
    success_url = '/movies'
    templates_name = 'movies/movies.html'    
       
    
def create (request):
    error = ''
    if request.method == "POST":
        form = MoviesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = 'Форма неверна'
        
    form = MoviesForm()
    data = {'form': form}
    return render (request, 'movies/create.html', data)

class SearchResultsView(ListView):
    model = Movies
    template_name = 'movies/search_results.html'
 
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movies.objects.filter(
            Q(title__icontains=query) | Q(original_lang_title__icontains=query)
        )
        return object_list