# -*- coding: utf-8 -*-

import pandas as pd

# 엑셀 파일 Read, Write 모듈 설치
# pip install xlrd
# pip install xlwt
# pip install openpyxl
# pip install xlrd xlwt openpyxl

input_file_name = "sales_2013.xlsx"

# pandas 모듈을 활용한 엑셀 파일 로딩 처리
# pandas 모듈의 read_excel 함수
# read_excel(엑셀파일명, sheetname="읽어올sheet이름")
data_frame = pd.read_excel(input_file_name, 
                           sheet_name="january_2013")

# pandas 모듈은 읽어온 데이터를 데이터프레임으로 저장합니다.
# (테이블의 구조를 가진 자료형)
# print(data_frame)
# print(data_frame["Invoice Number"])
# print(data_frame["Customer ID"])
# print(data_frame[["Customer ID","Customer Name"]])
# print(data_frame["Customer Name"][2])
# print(data_frame["Customer Name"][2:5])
# print(data_frame["Customer Name"][2:-1])
# print(data_frame["Customer Name"][-1:])

# print(data_frame["Customer ID"] >= 5000)
# print(data_frame[data_frame["Customer ID"]>=5000])

output_file_name = "sales_2013_copy_1.xlsx"
writer = pd.ExcelWriter(output_file_name)
data_frame.to_excel(writer, 
                    sheet_name="january_2013_copy",
                    index=True)
writer.save()
















