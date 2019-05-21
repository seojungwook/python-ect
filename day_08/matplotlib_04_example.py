# -*- coding: utf-8 -*-

# Name(X) Amount(Y)
import pandas as pd
from matplotlib import pyplot as plt

input_file_name = "sales_2013.xlsx"
df = pd.read_excel(input_file_name, 
                           sheet_name="january_2013",
                           index_col="Customer Name")
df_i = df.iloc[:, 2]
# pandas 데이타프레임 타입은 저장하고 있는 데이터를
# 시각화 할 수 있는 기능을 내장하고 있음
# 아래와 같이 plot 함수를 호출하면 인덱스는 X 데이터
# 각 데이터를 Y 데이터로 전달됩니다.
df_i.plot()

# 데이터프레임의 plot 함수를 호출한 이후에는 
# matplotlib 의 plt를 사용하여 각 설정이후
# 그래프를 출력할 수 있습니다.
plt.title("Sales Amount")
plt.xlabel("ID")
plt.ylabel("Amount")
plt.show()

#plt.title("Sales Amount")
#plt.xlabel("Name")
#plt.ylabel("Amount")
#plt.plot(df["Customer Name"], df["Sale Amount"], "y-.")
#plt.show()














