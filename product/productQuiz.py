from productFunc import *


while True:
    print('''
    1. 제품입력
    2. 제품목록
    3. 제품검색
    4. 제품수정
    5. 제품삭제
    6. 종료
    7. 테이블 생성
    ''')

    menu = input("메뉴를 입력하시오: ")
    if menu == '1':
        insert()
    elif menu == '2':
        select_all()
    elif menu == '3':
        select()
    elif menu == '4':
        update()
    elif menu == '5':
        delete()
    elif menu == '6':
        break
    elif menu == '7':
        create_table()
    else:
        print("메뉴를 잘못 선택하셨습니다.")