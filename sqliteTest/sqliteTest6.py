from sqliteDB import *
import sys



while True:
    print('''
    1. 테이블 생성
    2. 데이터 입력
    3. 데이터 수정
    4. 데이터 삭제
    5. 데이터 리스트
    6. 종료
    ''')
    menu = input()

    if menu=='1':
        create_table()
    elif menu=='2':
        insert_data()
    elif menu=='3':
        update_data()
    elif menu=='4':
        delete_data()
    elif menu=='5':
        select_data()
    elif menu=='6':
        sys.exit()
    else:
        print('메뉴 잘못 선택')
