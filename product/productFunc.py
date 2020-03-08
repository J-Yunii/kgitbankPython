import pymysql

def db_conn():
    conn = pymysql.connect(
        host = 'maria',
        user = 'root',
        password = 'qwer1234',
        db = 'test',
        charset = 'utf8'
    )
    return conn

def create_table():
    conn = db_conn()
    c = conn.cursor()

    sql = """drop table books"""
    c.execute(sql)

    sql = """create table if not exists books(
        name text,
        page integer,
        pub text,
        description text
    )"""
    c.execute(sql)

    conn.commit()
    conn.close()


def insert():
    conn = db_conn()
    c = conn.cursor()

    name = input('책 이름을 입력하시오: ')
    page = int(input('페이지 수를 입력하시오: '))
    pub = input('회사 이름을 입력하시오: ')
    descript = input('비고란을 입력하시오: ')

    data = [name, page, pub, descript]

    sql = """insert into books values(%s,%s,%s,%s)"""
    
    c.execute(sql,data)

    conn.commit()
    conn.close()

# 목록 전체 조회
def select_all():
    conn = db_conn()
    c = conn.cursor()

    sql = """SELECT * FROM books"""
    c.execute(sql)

    print(c.fetchall())
    conn.close()

# 제품 검색
def select():
    conn = db_conn()
    c = conn.cursor()

    input_name = input('검색할 도서명을 입력하세요: ')
    input_name = '%'+input_name+'%'

    sql = """SELECT * FROM books where name LIKE %s"""
    c.execute(sql,(input_name,))

    print(c.fetchall())

    conn.close()

# 데이터 수정
def update():
    conn = db_conn()
    c = conn.cursor()

    input_name = input('수정할 도서명을 입력해 주세요: ')
    update_item = input('수정할 항목을 입력해 주세요(name, page, pub, descript): ')
    update_contents = input('수정할 내용을 입력해 주세요: ')

    if update_item == 'page':
        update_contents = int(update_contents)
    
    

    sql = "UPDATE books SET " + update_item +" = %s"
    c.execute(sql,(update_contents,))

    conn.commit()
    conn.close()

# 데이터 삭제
def delete():
    conn = db_conn()
    c = conn.cursor()

    input_name = input("삭제할 도서명을 입력하시오: ")
    sql = """DELETE FROM books where name = %s"""
    c.execute(sql,(input_name, ))

    conn.commit()
    conn.close()

