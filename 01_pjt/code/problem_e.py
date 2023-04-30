import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    id_nums_key = []
    for i in range(len(movies)):
        id_nums_key.append(movies[i]['id'])
    # print(id_nums_key)
    open_1 = []
    name = []
    open_name = {}
    open_title = []
    for j in id_nums_key:
        
        movie = open(f'data/movies/{j}.json', encoding='utf-8')     # id숫자의 파일들을 연다
        movie_detail = json.load(movie)
        
        open_name[movie_detail.get("release_date")] =movie_detail.get("title")  # 개봉일과 제목을 가지는 딕셔너리를 만든다.

        
        a, mon, c =movie_detail.get("release_date").split("-")      #입력된 개봉일을 나누어 12월에 만들어 진것의 제목을 찾아 open_title에 넣는다
        if int(mon) == 12:
            open_title.append(open_name[movie_detail.get("release_date")])  #

    # print(open_title)
    return open_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))


2004-11-19