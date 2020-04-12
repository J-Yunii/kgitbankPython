import urllib
from bs4 import BeautifulSoup
import pandas as pd


def naverMovie():
    # def naverMovie
    url = 'https://movie.naver.com/movie/running/current.nhn'

    response = urllib.request.urlopen(url)
    # 뷰티풀 수프 개체 만들어짐
    navigator = BeautifulSoup(response, 'html.parser')
    table = navigator.select('ul.lst_detail_t1 li')
    movielist=[]

    # print(type(table))
    # print(table)
    for tt in table:
        # 클래스가 thumb .이니까
        # 이미지 소스 가지고 옴
        thumb = tt.select('div.thumb img')[0]['src']
        # print(thumb)
        # 제목 가져 옴
        title = tt.select('.tit a')[0].string
        # print(title)
        code = int(tt.select('.tit a')[0]['href'].split('=')[1])
        # print(code)
        # 상영시간 가져옴
        try:
            # 단계별로 확인하면서 작성하기
            time = int(tt.select('.info_txt1 dd')[0].text.split('|')[1].strip()[:-1])
        # 어떤 거는 앞쪽 게 없어서 맨 앞에 상영시간이 있음
        except:
            time = int(tt.select('.info_txt1 dd')[0].text.split('|')[0].strip()[:-1])
        # print(time)

        try:
            sdate = tt.select('.info_txt1 dd')[0].text.split('|')[2].strip()[0]
        except:
            sdate = tt.select('.info_txt1 dd')[0].text.split('|')[1].strip()[0]
        # print(sdate)

        # 관람 연령
        grade = tt.select('dt.tit span')[0].text
        # print(grade)

        # 무비 코드값만 달라짐!, 미리 빼놓은 코드 값으로 상세페이지 접속
        url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code={}'.format(code)
        response = urllib.request.urlopen(url)
        navigator = BeautifulSoup(response,'html.parser')

        try:
            # 총 관람객 수, 천 자리 단위 콤마 빼기
            audience =  int(navigator.select('div.step9_cont p.count')[0].text.split('(')[0][:-1].replace(",",""))
        except:
            # 총 관람객 수가 없을 때
            audience = 0
        # print(type(audience))
        # print(audience)

        try:
            summary=navigator.select('div.story_area h5.h_tx_story')[0].text.strip()
        except:
            summary=''
        # print(type(summary))
        # print(summary)

        movieinfo = {'code': code, 'title':title, "time":time, 'sdate':sdate,'grade':grade,'audience':audience,'summary':summary,'thumb':thumb}
        movielist.append(movieinfo)

    #print(movielist)
    # 데이터프레임으로 저장
    df = pd.DataFrame(movielist)

    # csv로 저장할 거면
    # df.to_csv('moviedata.csv')
    # df = pd.read_csv('moviedata.csv')

    #print(df)

    return df



