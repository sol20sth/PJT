from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer
from .serializers import MovieListSerializer, ActorListSerializer, ReviewListSerializer

# Create your views here.
@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actors_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def reviews_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movies_detail(request, movies_pk):
    movie = Movie.objects.get(pk=movies_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def actors_detail(request, actors_pk):
    actor = Actor.objects.get(pk=actors_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE', 'GET'])
def reviews_detail(request, reviews_pk):
    review = Review.objects.get(pk=reviews_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(request.data)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        message = {"deleted": f"review {reviews_pk} is deleted"}
        review.delete()
        return Response(message, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, movies_pk):
    movie = Movie.objects.get(pk=movies_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(movie=movie)
        return Response(serializer.data)
