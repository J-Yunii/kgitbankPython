#csv -> db
import sqlite3, csv


conn = sqlite3.connect('D:\pythonPRJ\kgitbankPython\sqliteTest\sup.db')
c = conn.cursor()
sql="""
create table if not exists sup
(
    sup_name varchar(20),
    invoice_number varchar(20),
    part_number varchar(20),
    cost float,
    date date
)"""
c.execute(sql)

# 안에 있는 데이터들 모두 삭제
sql = """delete from sup"""
c.execute(sql)

input_file = 'D:\pythonPRJ\kgitbankPython\sqliteTest\input.csv'
# 코딩문제가 뜨면 세번째 인자값에 UTF-8이나 기타 다른 인코딩법 넣어주기
f = open(input_file, 'r')
# 리더의 두번째 인자는 구분자, default값은 콤마
# file_reader = csv.reader(f, delimiter=';')
file_reader = csv.reader(f)
# next하면 cursor를 다음 줄로 넘겨줌
print(next(file_reader))
print('='*80)

# 자료 넣어주기
sql = """insert into sup values(?,?,?,?,?)"""

data = []
for row in file_reader:
    print(row)
    data.append(row)
c.executemany(sql,data)

conn.commit()
conn.close()