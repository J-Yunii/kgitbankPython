import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

# 여러 영화 코드를 가져와서 저장가능
# 페이지 값은 크롤링하면 시간 많이 걸려서
def Getdata(code_list,page=None):
    # 영화 코드
    code_list = code_list    
    # 현재 크롤링 중인 영화가 첫 번째 영화인지 여부
    # 파일로 저장할 때 쓰임 -> 첫 번째 영화는 파일을 만들어야 하므로
    # chk = False
    # 영화의 개수만큼 반복한다.
    df = pd.DataFrame()
    
    for code in code_list:
        # 1단계 : 해당 영화의 평점 페이지 수 계산, 페이지 당 10개 리뷰가 존재, 별점도 가져오기
        # 영화별 리뷰 페이지에 접속한다.
        site1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'.format(code)
        res1 = requests.get(site1)
        # 파일을 제대로 가져왔는지 체크
        if res1.status_code == requests.codes.ok:
            # html코드를 분석한다.
            # 객체화시킴
            bs1 = BeautifulSoup(res1.text, 'html.parser')
            # 평수
            score_total = bs1.find(class_='score_total')
            ems = score_total.find_all('em')
            # print(ems[0].text)
            # 페이지 수 계산 위해서 ,없애고 인트로 변환
            score_total = int(ems[0].text.replace(',', ''))
            print(score_total)
            # 페이지 수를 계산한다. 한 페이지당 10개
            pageCnt = score_total // 10
            print(pageCnt)
            # 나머지가 있으면 한 페이지를 더 추가!
            if score_total % 10 > 0:
                pageCnt += 1
            # 현재 페이지 번호
            # 페이지가 들어왔고 내가 입력한 페이지 값보다 페이지 카운터가 커야함
            # pageCnt 420페이지 다 뽑아서 크롤링 하면 시간 오래 걸림
            if page!=None and pageCnt>=page:
                pageCnt=page
                
            # print(pageCnt)
            now_page = 1

            # 2단계 : 평점 글 정보와 평점을 가져온다.
            while now_page <= pageCnt:
                sleep(0.5)
                
                # 요청 할 페이지의 주소
                # 나중에 format형식으로 바꾸기, 데이터 타입 맞추기 어려우니까
                # 영화 code값이랑 해당 페이지 값 넣어서 가져옴
                site2 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(code, now_page)
                res2 = requests.get(site2)
                if res2.status_code == requests.codes.ok:
                    # print('page: %d / %d' % (now_page, pageCnt))
                    bs2 = BeautifulSoup(res2.text, 'html.parser')
                    score_result = bs2.find(class_='score_result')
                    lis = score_result.find_all('li')
                    
                    for obj in lis:
                        # 평점
                        star_score = obj.find(class_='star_score')
                        star_em = star_score.find('em')
                        star_score = int(star_em.text)
                        # 평가글
                        score_reple = obj.find(class_='score_reple')
                        reple_p = score_reple.find('span')
                        score_reple = reple_p.text.strip()
                        # print(star_score, score_reple)
                        # 데이터를 누적한다
                        # 점수는 있지만 리뷰만 있으면 없앰, 관람객이라는 것도 없앰
                        if score_reple=='' or score_reple=='관람객':
                            continue
                        else:
                            df = df.append([[score_reple, star_score]], ignore_index=True)
                    now_page += 1
    df.columns = ['text', 'star']
    return df