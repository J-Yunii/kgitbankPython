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
def star_proprocessing(text) :
    value = int(text)
    if value <= 5 :
        return '0'
    else :
        return '1'

def step2_preprocessing():
    # 수집한 데이터를 읽어온다.
    df = pd.read_csv('./data/naver_star_data.csv')
    # 랜덤하게 섞는다.
    # print(df)
    # print('---------------------')
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    # print(df)

    # 전처리 과정
    df['text'] = df['text'].apply(text_preprocessing)
    df['star'] = df['star'].apply(star_proprocessing)
    # 학습 데이터와 테스트 데이터로 나눈다.
    text_list = df['text'].tolist()
    star_list = df['star'].tolist()

    text_train, text_test, star_train, star_test = train_test_split(text_list, star_list, test_size=0.3, random_state=0)
    #print(len(text_train))
    #print(len(text_test))
    #print(len(star_train))
    #print(len(star_test))

    # 저장한다.
    dic_train = {
        'text' : text_train,
        'star' : star_train
    }
    df_tran = pd.DataFrame(dic_train)

    dic_test = {
        'text' : text_test,
        'star' : star_test
    }
    df_test = pd.DataFrame(dic_test)

    df_tran.to_csv('./data/movie_train_data.csv', index=False, encoding='utf-8-sig')
    df_test.to_csv('./data/movie_test_data.csv', index=False, encoding='utf-8-sig')

