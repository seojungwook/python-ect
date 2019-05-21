# -*- coding: utf-8 -*-

import pandas as pd

input_file_name = "sales_2013.xlsx"

df = pd.read_excel(input_file_name, 
                   sheet_name="january_2013",
                   index_col=None)

# pandas dataframe 의 iloc 연산
# iloc[ 행의 정보(시작인덱스:종료인덱스) , [열의 정보] ]
# 열의 데이터가 하나인 경우 정수형으로 전달
# df.iloc[:, 1] -> 2번째 열을 추출
# 열의 데이터가 하나인 경우 리스트형으로 전달
# df.iloc[:, [1,4]] -> 2번째, 5번째 열을 추출
df_by_iloc = df.iloc[:, [1, 4]]

print(df_by_iloc)













