import json
import problem_b
from pprint import pprint


def movie_info(movies, genres):
    movie_list = []
    #함수 재사용
    for movie in movies:
        movie_list.append(problem_b.movie_info(movie, genres))

    return movie_list



if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
