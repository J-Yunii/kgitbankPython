# step2_preprocessing.py
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 평가 문자열 전처리
def text_preprocessing(text) :
    # 관람객이라는 글자로 시작하면 관람객을 제거한다.
    if text.startswith('관람객') :
        # old_str = text
        new_str = text[3:]
        # print('%s -> %s' % (old_str, new_str))
        return new_str
    else :
        return text

# 평점 전처리
def star_proprocessing(star) :
    value = int(star)
    # 평점이 5이하이면 0점, 6이상이면 1점
    if value <= 5 :
        return '0'
    else :
        return '1'

def step2_preprocessing():
    # 수집한 데이터를 읽어온다.
    df = pd.read_csv('./data/naver_star_data.csv')
    # 랜덤하게 섞는다. - 평점 좋은 영화, 평점 안좋은 영화를 섞어서 골고루 학습시키기 위해서
    # print(df)
    # print('---------------------')
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    # print(df)

    # 전처리 과정
    df['text'] = df['text'].apply(text_preprocessing)
    df['star'] = df['star'].apply(star_proprocessing)
    # 학습 데이터와 테스트 데이터로 나눈다. 리스트로 바꿔줘야 처리가 쉬움(나누기 위해서)
    text_list = df['text'].tolist()
    star_list = df['star'].tolist()

    # 함수에서 text_list가 x값 문제, star_list는 y값 답, 순서 유의
    # 테스트 사이즈 7:3정도로 나눔
    # 처음에 내는 문제 테스트 할것, 처음 문제 답, 테스트 문제 답
    text_train, text_test, star_train, star_test = train_test_split(text_list, star_list, test_size=0.3, random_state=0)
    # 학습시킬 문제
    # print(len(text_train))
    # 학습시킬 문제의 답
    # print(len(text_test))
    # print(len(star_train))
    # print(len(star_test))

    # 딕셔너리로 저장한다.
    dic_train = {
        'text' : text_train,
        'star' : star_train
    }
    # 다시 데이터 프레임으로 전환
    df_tran = pd.DataFrame(dic_train)

    dic_test = {
        'text' : text_test,
        'star' : star_test
    }
    # 데이터프레임 - csv에 저장하기 위해서, 판다스에서 쓰면 편함
    df_test = pd.DataFrame(dic_test)

    df_tran.to_csv('./data/movie_train_data.csv', index=False, encoding='utf-8-sig')
    df_test.to_csv('./data/movie_test_data.csv', index=False, encoding='utf-8-sig')

