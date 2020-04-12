# 테이블 생성 맨처음 한번 실행
from app import db

# conda install -c conda-forge flask_sqlalchemy로설치하기
db.create_all()