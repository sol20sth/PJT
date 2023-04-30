import requests
from pprint import pprint

def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    # search Movies api를 찾은뒤 더찾을 파리미터로 제목인 {title}을 집어넣어 설정
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=0dff247d313e11da8a33fd252d521489&language=en-US&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    first = []
    
    #예외처리 results의 0번쨰가 없는 값들이 존재해서 만약 존재하지 않다면 None를 반환
    try:
        movie_id = response['results'][0].get('id')
    except IndexError:
        return None
    # URL2로 Get Recommendations를 가져와서 movie_id 와 api를 넣어준다. 위에 변수를 이름 같게 만들어서 movie_id가 돌아감
    # 변수이름 바뀌면 바뀐걸로 집어넣기
    URL2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=0dff247d313e11da8a33fd252d521489&language=ko&page=1'
    # print(result2)
    response2 = requests.get(URL2).json()
    # 받아온 추천목록의 'results'에있는 요소들의 'title'값들을 새리스트에 집어넣는다. 그리고 반환
    for name in response2['results']: 
        first.append(name['title'])
    return first

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

