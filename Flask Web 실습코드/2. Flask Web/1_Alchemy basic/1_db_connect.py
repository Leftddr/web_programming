import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root',
                       db='madang', charset='utf8')

# Connection 으로부터 Cursor 생성
# curs : array based cursor (default)
curs = conn.cursor()

# SQL문 실행
sql = "select * from customer"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)  # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '박지성', '영국 맨체스타', '000-5000-0001')
# print(rows[1])  # 두번째 row: (2, '김연아', '대한민국 서울', '000-6000-0001')

# Connection 닫기
conn.close()