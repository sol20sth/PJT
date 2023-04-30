from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Movie, Genre

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,

    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = Genre.objects.filter(movie=movie)
    context = {
        'movie' : movie,
        'genres' : genres,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        movies = Movie.objects.all()
        genres = Genre.objects.all()
        movies = sorted(movies, key=lambda x: x.vote_count)[:10]
        context = {
            'movies' : movies,
            'genres' : genres,
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')


