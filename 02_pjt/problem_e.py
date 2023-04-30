import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # Search Movies api를 URL에 넣는다.
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=0dff247d313e11da8a33fd252d521489&language=en-US&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    # 똑같이 response['results'][0]가 없을경우 때문에 예외처리
    try:
        movie_id = response['results'][0].get('id')
    except IndexError:
        return None
    # Get Credits -출연진과 스테르 목록 가져오고 내api 와 movie_id를 집어넣기
    URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=0dff247d313e11da8a33fd252d521489&language=en-US'
    response_2 = requests.get(URL2).json()
    # print(response_2)
    name = []
    crew = []
    #출연진과 스테프 목록의 'cast'안에있는 i[cast_id]가 10보다 작을떄 새로운 리스트에 추가
    for i in response_2['cast']:
        if i['cast_id'] < 10:
            name.append(i['name'])
    #출연진과 스테프 목록의 'crew'안에있는 i[known_for_department]가 Directing일때 새로운 리스트에 추가
    for i in response_2['crew']:
        if i['known_for_department'] == 'Directing':
            crew.append(i['name'])
    #위에서 만든 name, crew를 새 딕셔너리의 value값으로 집어넣는다. >> key는 'cast', 'directing
    dict_name = {}
    dict_name['cast '] = name
    dict_name['directing '] = list(set(crew)) # 동일한 요소지우기위해 set으로 바꾼뒤 list로 다시바꿈
    return dict_name


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
