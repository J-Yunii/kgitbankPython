import pymysql

# 호스트: 마리아db가 작업하고 있는 컴에 설치되어 있으면 localhost, 사용자는 root, 비밀번호는 설치 당시 root 비밀번호, 접속할 db 이름,
# cursorclass는 라이브러리에서 cursor받아옴 DictCursor는 딕셔너리 형태로 리턴함
# conn = pymysql.connect(host='localhost',


# 여기서는 가상 컴으로 마리아 컴과 아나콘다 컴이 따로 있으므로
# host 이름은 처음 이미지 설치할 때 설정해준 이름으로 해준다.
conn = pymysql.connect(
    host='maria',
    user='root',
    password='qwer1234',
    db='test',
    cursorclass=pymysql.cursors.DictCursor)

c=conn.cursor()
c.execute("""
create table if not exists stocks
(date text,trans text,symbol text,qty real,price real) 
""")
c.execute('''insert into stocks values
('2020-03-07','buy','rhat',100,35.14)''')

conn.commit()
conn.close()
