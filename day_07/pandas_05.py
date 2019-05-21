# -*- coding: utf-8 -*-

import pandas as pd

input_file_name = "sales_2013.xlsx"

df = pd.read_excel(input_file_name, 
                   sheet_name="january_2013",
                   index_col=None)

# pandas dataframe의 loc
# loc[ 행의 정보(시작인덱스:종료인덱스) , [열의 헤더 이름 정보] ]
# 열의 데이터가 하나인 경우 문자열형으로 전달
# df.iloc[:, "Customer Name"] -> "Customer Name" 열을 추출
# 열의 데이터가 다수개인 경우 리스트형으로 전달
# df.iloc[:, ["Customer ID","Customer Name"]] -> 
# Customer ID, Customer Name 열을 추출
df_by_loc = df.loc[:, ["Customer ID","Customer Name"]]
print(df_by_loc)






























