# -*- coding: utf-8 -*-

import pymysql

# 데이터베이스 처리
# 파이썬에서는 다양한 데이터베이스 벤더에 대한 
# 모듈을 사용할 수 있습니다.
# (데이터베이스 벤더사에 따른 모듈을 설치를 진행)

# 데이터베이스 프로그래밍 과정
# 1. 데이터베이스 연결 객체 생성
db = pymysql.Connect(host="localhost",
                port=3306,
                user="root",
                passwd="1234",
                db="sakila")
# 2. 데이터베이스 서버에 쿼리문을 실행할 수 있는
# 객체를 생성(데이터베이스 연결 객체로 부터 생성)
cursor = db.cursor()
# 3. SQL문 작성
# - 문자열로 작성
# - 대다수의 데이터베이스 처리 모듈은 ; 생략이 가능
sql = """
    select *
    from rental
"""
# 4. SQL문 실행
cursor.execute(sql)
# pymysql의 cursor 객체는 쿼리의 실행 결과 레코드 수를
# rowcount를 통해서 확인할 수 있음
# print("실행 결과 : ", cursor.rowcount)

# 5. SQL문의 실행 결과를 반복문을 통해서 확인
# - Select 절의 실행 결과를 반환받는 방법
# - fetchall 메소드
#  검색된 모든 결과를 한번에 전송받는 메소드
#  검색된 데이터가 많이 않은 경우 효과적
result = cursor.fetchall()
# fetchall을 사용하는 경우 각각의 레코드 단위로
# 데이터를 처리하기위해서 반복문을 사용
# 각 반복은 한개의 데이터를 의미
for record in result :
    # 각 레코드의 데이터는 인덱스를 활용하여
    # 추출할 수 있음
    print(f"{record[0]},{record[3]},{record[6]}")

# 6. 리소스 해제 처리 (close 메소드 호출)
cursor.close()
db.close()















