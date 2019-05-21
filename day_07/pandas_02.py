# -*- coding: utf-8 -*-

import pandas as pd

input_file_name = "sales_2013.xlsx"

df = pd.read_excel(input_file_name, 
                   sheet_name="january_2013",
                   index_col="Customer ID")

# print(df)

# 검색할 정보 설정
dates = ['2013-01-01', '2013-01-11', '2013-01-31']
df_condition = df[["Customer Name", "Sale Amount"]][
        df["Purchase Date"].isin(dates)]

print(df_condition)
#print(df_condition[ ["Customer Name", "Sale Amount"] ])

output_file_name = "sales_2013_copy_2.xlsx"
writer = pd.ExcelWriter(output_file_name)
df_condition.to_excel(writer, 
                    sheet_name="january_2013_copy",
                    index=False)
writer.save()











