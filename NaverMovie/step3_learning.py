# step3_learning.py
# 선형회귀가 베이스, LogisticRegression은 예 아니오로 구분
from sklearn.linear_model import LogisticRegression
# 글자이므로 tfid를 통해서 수치화
from sklearn.feature_extraction.text import  TfidfVectorizer
# 데이터를 벡터라이즈 해서 공부시켜야 하는데
# pipeline을 쓰면 단계별로 묶어서 관리하기가 편함 파이프만 유지하면 됨
from sklearn.pipeline import Pipeline
# 정확도 체크용 라이브러리
from sklearn.metrics import accuracy_score
# 파이썬에서 저장관리하는 라이브러리
import pickle
from time import time
import pandas as pd
# 한국어 자연어 처리
from konlpy.tag import *

# konlpy의 명사 추출 객체 생성
okt = Okt()

def tokenizer(text) :
    return okt.morphs(text)

def step3_learning() :
    # 데이터를 읽어온다.
    # 타입이 데이터 프레임
    train_df = pd.read_csv('./data/movie_train_data.csv')
    test_df = pd.read_csv('./data/movie_test_data.csv')

    # 리스트로 바꿔서 넣어주기
    X_train = train_df['text'].tolist()
    y_train = train_df['star'].tolist()

    X_test = test_df['text'].tolist()
    y_test = test_df['star'].tolist()
    # 학습을 위한 객체를 생성한다.
    # tokenizer는 위에서 만든 함수, 
    # 글자 가져와서 수치화시킴
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)

    # LogisticRegression 안의 인자값은 데이터 특성에 따라 조절

    logistic = LogisticRegression(C=10.0, penalty='l2', random_state=0,solver='lbfgs')
    # 수치화 시킨 글자를 넣어줌
    # 리스트로 처음에 tfidf 처리하고 두번째로 logistic처리하고
    pipe = Pipeline([('vect', tfidf), ('clf', logistic)])

    # 학습한다.
    stime = time()
    print("학습 시작")
    pipe.fit(X_train, y_train)
    print("학습 종료")
    etime = time()
    print("총 학습 시간 : %d" % (etime - stime))

    # 학습 정확도 측정
    # 가설에 의해서 나온것이 y_pred
    y_pred = pipe.predict(X_test)
    # 가설(에 의해 나온 답)과 테스트 값(정답)이 얼마나 다른지 계산 
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))

    # 객체 저장
    with open('./data/pipe.dat', 'wb') as fp :
        pickle.dump(pipe, fp)

    print('저장완료')
