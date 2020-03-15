# 터미널에 $sudo bash
# $ conda install pymysql
import pymysql
connection = pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    # 문장 끝나면 커서 반납함!!
    with connection.cursor() as cursor:
        sql = '''
            DROP TABLE IF EXISTS users;
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
            CREATE TABLE IF NOT EXISTS users(
                userid varchar(20) primary key,
                userpw varchar(20) not null,
                username varchar(20) not null,
                userage int,
                usermail varchar(20),
                useradd varchar(50),
                usergender varchar(20),
                usertel varchar(20))
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
        INSERT INTO users VALUES(
            'hong',
            '1234',
            '홍길동',
            23,
            'hong@gmail.com',
            '부산시 동구 수정동',
            'male',
            '010-1234-1234');
        '''
        cursor.execute(sql)
        connection.commit()

    with connection.cursor() as cursor:
        sql = '''
            SELECT * FROM users;
        '''
        cursor.execute(sql)
        print(cursor.fetchall())

# 반드시 실행되는 구문
finally:
    connection.close()
