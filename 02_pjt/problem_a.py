import requests


def popular_count():
    pass 
    # https://www.themoviedb.org/settings/api 사이트에서 내게 해당하는 api 키를 가져오고 URL을 api요청주소로 설정 후 내 api를 입력한다.
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=0dff247d313e11da8a33fd252d521489&language=en-US&page=1' 
    # URL을 요청한고 변수로 잡는다.
    response = requests.get(URL).json()
    # print(response)
    # URL의 'result'의 키를 results로 잡는다
    results = response.get('results')
    # print(results)
    # 길이를 구해서 영화목록 개수를 반환한다.
    return len(results)
   
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
