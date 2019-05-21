# -*- coding: utf-8 -*-

# 성적 처리를 위해서 3과목의 성적을 입력받고
# 총점과, 평균을 저장 (파일)
count = 3
scores = []
tot = 0
avg = None

for i in range(count) :
    scores.append(int(input(f"{i+1} 번째 성적 : ")))
    # tot += scores[i]
    tot += scores[-1]

avg = tot / count
print(f"총점 : {tot}점, 평균 : {avg:.2f}점")

# 문자열 결합은 문자열 끼리만 가능하기 때문에
# 숫자인 경우 에러 발생
#output_data = ",".join(scores)

# CSV 포맷으로 데이터 생성
# 숫자로 구성된 리스트의 모든 요소를 문자열로 변경
output_data = ",".join(map(lambda x:str(x), scores))
output_data += f",{tot},{avg:.2f}\n"
print(output_data)

# 파일에 저장하기 위한 변수
output_file_name = "data/file_05.txt"
# a 모드 : append 모드
# (기존의 데이터를 삭제하지 않고 유지하는 모드)
output_file = open(output_file_name, "a")
output_file.write(output_data)
output_file.close()















