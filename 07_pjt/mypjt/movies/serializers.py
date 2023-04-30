from .models import Movie, Actor, Review
from rest_framework import serializers
class Movie1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)
        
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)
        
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
class Actor1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = Movie1Serializer(read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'movie', 'title', 'content', )

class MovieSerializer(serializers.ModelSerializer):
    actors = Actor1Serializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        
class ActorSerializer(serializers.ModelSerializer):
    movies = Movie1Serializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'