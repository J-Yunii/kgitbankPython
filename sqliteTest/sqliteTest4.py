import sqlite3

conn = sqlite3.connect('D:\pythonPRJ\kgitbankPython\sqliteTest\example.db')
c = conn.cursor()
data = [
    ('2020-03-07','buy','rhat',100,35.14),
    ('2020-02-09','buy','net',80,24.95),
    ('2020-03-05','buy','com',54,220.55),
    ('2020-01-18','buy','rhat',210,35.14)
    ]

sql = """insert into stocks values(?,?,?,?,?)"""
c.executemany(sql, data)

conn.commit()
conn.close()