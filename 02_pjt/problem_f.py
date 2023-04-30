
#최신영화 뽑아내보기...
import requests


def open_name():
    pass 
    #영화진흥위원회에서 일별 박스오피스 서비스 데이터를 받아온다
    URL = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20120101' 
    
    response = requests.get(URL).json()
    print(response)
    # 받아온 데이터에서 dict(boxOfficeResult) 자료에서 dict(dailyBoxOfficeList)를 추출한다.
    daily_list = response.get('boxOfficeResult').get('dailyBoxOfficeList')
    # print(daily_list)
   # 필요한 변수값 초기화
    open = []
    name = []
    new_list = []
    movie_new = {}

    for i in range(len(daily_list)):
        open.append(daily_list[i]['openDt'])    # 받아온자료에서 오픈날자만 뽑아서 리스트화
    # print(open)
    for i in range(len(daily_list)):
        name.append(daily_list[i]['movieNm'])   # 받아온자료에서 이름만 뽑아서 리스트화
    # print(name)
    for j in range(len(daily_list)):
        year, mon, day =map(int, open[j].split('-'))    #날짜를 년 월 일 로 나누어
    for k in range(len(open)):                          #날짜 : 이름 형식으로 딕셔너리에 넣는다
        movie_new[open[k]] = name[k]
    
    for date in open:                       # 2011년 미만이면 최신영화 아닌걸로 판단하고 제거
        year, mon, day = map(int, date.split('-'))
        if year < 2011:
            movie_new.pop(date)
    # print(movie_new)
    final = list(movie_new.values())        # 남은 자료들중 제목만 추출
    return final
   
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    open_name 최신영화 제목 반환
    """
    print(open_name())

    
