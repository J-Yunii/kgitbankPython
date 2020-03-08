import pymysql

conn = pymysql.connect(
    host = 'maria',
    user = 'root',
    password = 'qwer1234',
    db = 'test',
    charset = 'utf8'
    # cursorclass = pymysql.cursors.DictCursor
)

c = conn.cursor()

data = [
    ('2020-03-07','buy','rhat',100,35.14),
    ('2020-02-09','buy','net',80,24.95),
    ('2020-03-05','buy','com',54,220.55),
    ('2020-01-18','buy','rhat',210,35.14)]

sql = """insert into stocks values(%s,%s,%s,%s,%s)"""

# 실행할 문장이 여러 개
# 첫번째 인자는 쿼리문 두번쨰 인자는 데이터
c.executemany(sql,data)
conn.commit()

# 가격 순으로 정리해서 보여줌
# order by default값은 오름차순
sql = """select * from stocks order by price desc"""
c.execute(sql)
print(c.fetchall())

conn.close()

