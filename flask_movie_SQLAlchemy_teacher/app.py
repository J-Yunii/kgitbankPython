from flask import Flask,request,render_template,redirect,url_for,jsonify
from soynlp.noun import LRNounExtractor
# 네이버무비: 크롤링, 무비스타:영화평끌어오는, 무비워드클라우드: 워드클라우드 끌어오는 것
import naver_movie,movie_start,movie_wordcloud
import pandas as pd

app=Flask(__name__)

import sqlalchemy as sa

# 판다스랑 마리아 디비 연결
metadata = sa.MetaData()
data_table = sa.Table('movie', metadata,
                     sa.Column('code', sa.Integer, primary_key = True),
                     sa.Column('title', sa.String),
                     sa.Column('time', sa.Integer),
                     sa.Column('sdate', sa.String),
                     sa.Column('grade', sa.String),
                     sa.Column('audience', sa.Integer),
                     sa.Column('summary', sa.String),
                     sa.Column('thumb', sa.String)
)

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:qwer1234@maria/test", encoding='utf-8')

@app.route('/')
def index():
    return render_template('bootstraptest.html')

@app.route('/movieinfo')
def movieinfo():
    return render_template('movieinfo.html')

# ajax로 moviesearch를 호출, get방식으로 호출하니 method인자 적을 필요 없음
@app.route('/moviesearch')
def moviesearch():
    try:
        df = naver_movie.naverMovie()
        # if_exists = True => 엎어쓰겠다.
        # 데이터프레임 데이터베이스에 넣어줌
        df.to_sql(name='movie', con=engine, if_exists='replace',index=False)
        message = "영화 데이터 크롤링에 성공했습니다."
    except:
        message="데이터를 가져오는 데 실패했습니다."
    return message


@app.route('/movielist')
def movielist():
    # 데이터 프레임으로 읽어온 걸, 딕셔너리로 바꿔서(key값 쓰기 위해서) HTML로 보냄
    df=pd.read_sql('movie',engine)
    # orient='record' : 행 단위로 읽음
    movielist= df.to_dict(orient="record")
    # html에서 진자 이용해서 반복문으로 읽음
    return render_template('movielist.html', movielist=movielist )

# 링크 걸어서 가져올 때는 get방식이 나음
# url로 가져오자 편하니까
# 인자값으로 code 넣어주는 거 빼먹지 말기
@app.route('/content/<code>')
def content(code):
    # 하나만 들고옴
    # c: 컬럼.code
    df=pd.read_sql_query(sa.select([data_table]).where(data_table.c.code == code) , engine)
    movielist= df.to_dict(orient="record")
    # df1=movie_start.Getdata([code],10)
    # movie_wordcloud.displayWordCloud(str(code),' '.join(df1['text'])) 
    return render_template('content.html', movielist=movielist )

@app.route('/movieword/<code>')
def movieword(code):
    df1=movie_start.Getdata([code])
    # 명사만 뽑는 작업 나중에 코드 쓰기
    noun_extractor = LRNounExtractor(verbose=True)
    noun_extractor.train(df1['text'])
    nouns = noun_extractor.extract()
    # 명사들을 연결해서 워드클라우드로 뽑음
    movie_wordcloud.displayWordCloud(str(code),' '.join(nouns))    
    return "ok"

@app.route('/moviechart/<code>')
def moviechart(code):
      
    return "ok"


if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8890)