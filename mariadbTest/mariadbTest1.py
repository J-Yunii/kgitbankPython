import pymysql

# 호스트: 마리아db가 작업하고 있는 컴에 설치되어 있으면 localhost, 사용자는 root, 비밀번호는 설치 당시 root 비밀번호, 접속할 db 이름,
# cursorclass는 라이브러리에서 cursor받아옴 DictCursor는 딕셔너리 형태로 리턴함
conn = pymysql.connect(host='localhost',user='root',
password='qwer1234',db='test', cursorclass=pymysql.cursors.DictCursor)

cur=conn.cursor()
