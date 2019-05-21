# -*- coding: utf-8 -*-

# 구구단의 내용을 data/file_02_gugudan.txt에
# 출력하세요.

output_file_name = "data/file_02_gugudan.txt"
output = open(output_file_name, "w")

# 파이썬에서는 리스트 타입의 객체를 활용하여
# 파일에 일괄적으로 출력할 수 있습니다.
output_data = []

for i in range(2, 10) :
    output_data.append(f"{i}단을 출력합니다.")
    for j in range(1,10) :
        output_data.append(f"{i} * {j} = {i*j}")
    output_data.append("")

#output.writelines(output_data)
output.writelines(map(lambda x:x+"\n",output_data))
    
#for i in range(2, 10) :
#    output.write(f"{i}단을 출력합니다.\n")
#    for j in range(1,10) :
#        output.write(f"{i} * {j} = {i*j}\n")
#    output.write("\n")

output.close()










