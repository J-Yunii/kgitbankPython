import pymysql

conn = pymysql.connect(
    host = 'maria',
    user = 'root',
    password = 'qwer1234',
    db = 'test',
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor
)

c = conn.cursor()

c.execute("""
create table if not exists stocks
(date text,trans text,symbol text,qty real,price real) 
""")
c.execute('''insert into stocks values
('2020-03-07','buy','rhat',100,35.14)''')


symbol = input('symbol을 입력하세요: ')
sql = """select * from stocks where symbol='%s' """%symbol
# ?는 여기서 안됨... 안되나? 몰랑
# sql = """select * from stocks where symbol=? """

c.execute(sql)
print(c.fetchall())


conn.commit()
conn.close()