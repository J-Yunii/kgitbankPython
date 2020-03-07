import sqlite3

conn = sqlite3.connect('D:\pythonPRJ\kgitbankPython\sqliteTest\example.db')
c = conn.cursor()

c.execute('''select * from stocks''')
# fetch는 db 쿼리문 결과를 데이터 한 개만 터미널에 찍어줌
# fetchall은 모든 db 결과문을 찍어줌
print(c.fetchone())
# 숫자 만큼 결과 나옴
print(c.fetchmany(3))

symbol = 'com'
# 직접 symbol을 입력할 수도 있음
symbol = input('symbol을 입력하세요: ')

# 쿼리문 변수로 빼기 - 기니까 보기좋게 하기 위해서
# 데이터 타입 맞추기가 까다로울 수 있음 아래처럼 sql문을 받을 경우
sql = """select * from stocks where symbol='%s' """%symbol
# ?는 sqlite에서 지원 -> 오라클은 오라클 library, mysql, mariadb도 마찬가지
# 다른 데서는 지원안 할 수도 있음 그럴 땐 위의 구문처럼 작성하기
sql = """select * from stocks where symbol=? """

# 두번째 인자값은 튜플 or 리스트로 받음
# 튜플은 인자가 하나일 때 콤마 꼭!!
c.execute(sql, (symbol, ))
print(c.fetchall())
# select는 보여주기만 하므로 commit할 필요 없음
conn.close()