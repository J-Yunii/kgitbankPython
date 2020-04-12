# step4_usgin.py
# from sklearn.linear_model import LogisticRegression
# from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle
from time import time
import pandas as pd
# from konlpy.tag import *

def step4_using() :
    # 데이터를 읽어온다.
    with open('./data/pipe.dat', 'rb') as fp :
        pipe=pickle.load(fp)

    # 학습 정확도 측정
    y_pred = pipe.predict(["노잼"])
    print(y_pred)
    y_pred = pipe.predict(["정말 흥미진진함"])
    print(y_pred)
    y_pred = pipe.predict(["우와 정말 재미있어요. 한번더 보고 싶어요"])
    print(y_pred)
    # print('정확도 : %.3f' % accuracy_score(y_test, y_pred))
