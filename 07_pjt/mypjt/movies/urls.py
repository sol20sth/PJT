from django.urls import path
from movies import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.movies_list),
    path('movies/<int:movies_pk>/', views.movies_detail),
    path('actors/', views.actors_list),
    path('actors/<int:actors_pk>/', views.actors_detail),
    path('reviews/', views.reviews_list),
    path('reviews/<int:reviews_pk>/', views.reviews_detail),
    path('movies/<int:movies_pk>/reviews/', views.create_review),
]
