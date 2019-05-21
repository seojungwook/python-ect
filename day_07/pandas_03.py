# -*- coding: utf-8 -*-

import pandas as pd

input_file_name = "sales_2013.xlsx"

df = pd.read_excel(input_file_name, 
                   sheet_name="january_2013",
                   index_col=None)

#print(type(df["Customer Name"]))
#print(type(str(df["Customer Name"])))
#print(str(df["Customer Name"]))
#print(list(str(df["Customer Name"])))

# pandas 데이터프레임 객체에 대해서
# str속성에 접근하면 해당 컬럼의 데이터에
# 문자열 메소드를 실행한 결과를 반환받을 수 있습니다.
#print( df["Customer Name"].str.startswith("J") )
#print( df["Customer Name"].str.endswith("s") )
#print( df["Customer Name"].str.replace(" ", "") )

df_condition = df[
        map(lambda x:x!=-1, df["Customer Name"].str.find("J"))
        #df["Customer Name"].str.startswith("J")
        #df["Customer Name"].str[0] == "J"
        #df["Customer Name"].str[0].any(("J", "M"))
        ]

print(df_condition)
















