import sqlite3

conn = sqlite3.connect('D:\pythonPRJ\kgitbankPython\sqliteTest\example.db')
c = conn.cursor()
# execute안에는 실행 할 쿼리문 작성
# insert into를 통해 아까 만든 stocks table에 데이터 입력 문자열은 따옴표안에(작은 따옴표 쓰기)
c.execute('''insert into stocks values
('2020-03-07','buy','rhat',100,35.14)''')
# 반드시 commit 하기 
conn.commit()
conn.close()