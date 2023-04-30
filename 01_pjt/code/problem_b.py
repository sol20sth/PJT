import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    movie_a =['id' ,'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    movie_dict = {}
    for i in movie_a:
        movie_dict[i] = movie[i]
    # pprint(movie_di)
    # print(genres)
    genre_ids = movie["genre_ids"]
    movie_dict["genre_names"] = []
    #영화의 장르 아이디를 가지고
    #장르의 이름을 가져올 수 있는지
    for id in genre_ids:
        # print(id)
    #장르 id와 일치하는 장르 정보가 있으면 "name" 값 추출
        for genre in genres:
            if id == genre["id"]:
                #id를 찾았으니 그 id의 장르 이름을 추가
                movie_dict["genre_names"].append(genre["name"])

    return movie_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
