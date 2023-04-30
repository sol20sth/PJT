import json


id_nums_key = []
for i in range(len(movies)):
    id_nums_key.append(movies[i]['id'])
open_1 = []
name = []
open_name = {}
open_title = []
for j in id_nums_key:
    
    movie = open(f'data/movies/{j}.json', encoding='utf-8')
    movie_detail = json.load(movie)
    
    open_name[movie_detail.get("release_date")] =movie_detail.get("title")
    
    a, mon, c =movie_detail.get("release_date").split("-")
    if mon == 12:
        open_title.append(open_name[movie_detail.get("release_date")])
print(open_title)

