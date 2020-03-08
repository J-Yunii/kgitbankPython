import sqlite3

def db_conn():
    conn = sqlite3.connect('D:\pythonPRJ\kgitbankPython\sqliteTest\\book.db')
    return conn

def create_table():
    conn = db_conn()
    cur=conn.cursor()
    sql="""
    create table if not exists books(
        title text,
        pub_date text,
        pub text,
        page integer,
        recommend text
    )"""
    cur.execute(sql)

    conn.commit()
    conn.close()
    print('테이블 생성 완료')

def insert_data():
    conn = db_conn()
    cur = conn.cursor()
    title = input("책 제목: ")
    pub_date = input('출판일: ')
    pub = input('출판사: ')
    pages = int(input('총페이지: '))
    recommend = input('비고: ')

    data = [title, pub_date, pub, pages, recommend]
    sql = """insert into books values(?,?,?,?,?)"""

    cur.execute(sql,data)
    conn.commit()
    conn.close()

def select_data():
    conn = db_conn()
    cur = conn.cursor()

    # 제목을 조건으로 줄 거임
    title = input('찾고자 하는 책 제목: ')
    # 와일드 카드 %는 any를 뜻함, _는 any이나 한 자리를 뜻함(비어 있으면 안됨)
    title='%'+title+'%'
    # like 주의: 부분적으로 일치하는 컬럼을 찾을 때 사용됨
    sql = """select * from books where title like ?"""

    # ?에는 title이 들어감 / 두번째 인자값은 튜플 or 리스트로 받기
    cur.execute(sql,(title,))
    print(cur.fetchall())
    conn.close()

# 집에서 해보기
def update_data():
    pass

# 집에서 해보기
def delete_data():
    conn = db_conn()
    cur = conn.cursor()

