# word_tokenizer.py
from konlpy.tag import *
import pandas as pd

# 한글 형태소 분석을 위한 객체를 생성
okt = Okt()

def tokenizer_morphs(text):
    return okt.morphs(text)

def word_tokenizer() :
    train_df = pd.read_csv('./data/movie_train_data.csv')
    train_df['text_token'] = train_df['text'].apply(tokenizer_morphs)
    print(train_df['text_token'])

