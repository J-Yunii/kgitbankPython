import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

# sqlite는 파일상태로 관리됨, 파일 자체를 db로 봄
# 경로를 conn변수에 넣어줌
conn = sqlite3.connect('D:\pythonPRJ\kgitbankPython\sqliteTest\example.db')
# 변수에 커서 받아오기: 커서를 통해 명령 실행
c = conn.cursor()
# db안에 테이블 생성하기(관계형 데이터베이스)
# stocks이라는 table만들기(table이 없다면)
# 컬럼, 컬럼 자료형 적어주기
c.execute('''create table if not exists stocks
(date text,trans text,symbol text,qty real,price real)''')
# 변경사항 저장
conn.commit()
# 연결 끊기(파일 형태라 연결되어 있으면 동시접속 불가)
conn.close()

