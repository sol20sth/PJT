import json


def max_revenue(movies):
    
    id_nums_key = []
    for i in range(len(movies)):
        #movies에 들어간 갯수만큼 id의 갯수를 뽑아낸다.
        id_nums_key.append(movies[i]['id'])   
    # print(id_nums_key)
    good = []
    name = []
    good_name = {}
    for j in id_nums_key:
        
        movie = open(f'data/movies/{j}.json', encoding='utf-8')  #id의 숫자들을 제목으로 가지는.json파일을 len(id갯수)만큼 연다
        movie_detail = json.load(movie)                            
        movie_detail.get("revenue")
        good.append(movie_detail.get("revenue"))            # 수익과 제목을 가지는 list를 만든다수익과 제목을 가지는 dict를 만든다.  
        name.append(movie_detail.get("title"))
        good_name[movie_detail.get("revenue")] =movie_detail.get("title")   #수익과 제목을 가지는 dict를 만든다.

    # print(good)
    # print(name)
    # print(good_name)
    
    gooood = max(good)      #최대 수익
    # print(gooood)
    # print(good_name[gooood])
    return good_name[gooood]    #최대수익 리턴
    

    
    # print(movie_detail)

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
