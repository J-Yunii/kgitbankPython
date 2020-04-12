# step3_learning.py
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle
from time import time
import pandas as pd
from konlpy.tag import *

okt = Okt()

def tokenizer(text) :
    return okt.morphs(text)

def step3_learning() :
    # 데이터를 읽어온다.
    train_df = pd.read_csv('./data/movie_train_data.csv')
    test_df = pd.read_csv('./data/movie_test_data.csv')

    X_train = train_df['text'].tolist()
    y_train = train_df['star'].tolist()

    X_test = test_df['text'].tolist()
    y_test = test_df['star'].tolist()
    # 학습을 위한 객체를 생성한다.
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)

    logistic = LogisticRegression(C=10.0, penalty='l2', random_state=0,solver='lbfgs')
    pipe = Pipeline([('vect', tfidf), ('clf', logistic)])

    # 학습한다.
    stime = time()
    print("학습 시작")
    pipe.fit(X_train, y_train)
    print("학습 종료")
    etime = time()
    print("총 학습 시간 : %d" % (etime - stime))

    # 학습 정확도 측정
    y_pred = pipe.predict(X_test)
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))

    # 객체 저장
    with open('./data/pipe.dat', 'wb') as fp :
        pickle.dump(pipe, fp)

    print('저장완료')
