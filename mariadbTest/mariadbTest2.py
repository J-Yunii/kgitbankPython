import pymysql

conn = pymysql.connect(
    host = 'maria',
    user = 'root',
    password = 'qwer1234',
    db = 'test',
    # 한글 안깨지게 하기 위해서
    charset='utf8',
    # default 값은 list, dict가 key값이 있어 보기가 편하므로 변경해줌
    cursorclass = pymysql.cursors.DictCursor
)
c = conn.cursor()
sql = """select * from stocks"""
c.execute(sql)
print(c.fetchall())
conn.close()