# -*- coding: utf-8 -*-

# 사용자에게 5개의 성적을 입력받은 후,
# 각 성적의 그래프를 출력하세요.
# 성적의 최대값과, 최소값에 대해서 어노테이션을
# 추가하세요.
indexs = list(range(1,6))
# X 축의 데이터가 숫자로 지정되면 중간단위의
# 값이 출력되므로 문자열로 변경처리
indexs = list(map(lambda x : str(x), indexs))

scores = []
for i in range(1, len(indexs) + 1) :
    temp = int(input(f"{i}번째 성적입력 : "))
    scores.append(temp)
    
annotateInfo = {"max_score":max(scores),
                "min_score":min(scores),
                "max_index":1,
                "min_index":1}

for i in range( 1, len(indexs) ) :
    if scores[i] == annotateInfo["max_score"] :
        annotateInfo["max_index"] = i
    if scores[i] == annotateInfo["min_score"] :
        annotateInfo["min_index"] = i

from matplotlib import pyplot as plt
plt.title("Scores")
plt.xlabel("Index")
plt.ylabel("Score")
plt.plot(indexs, scores, "-.oc")

plt.ylim(min(scores)-15, max(scores)+15)

plt.annotate("Max Score", 
             xy=(annotateInfo["max_index"],max(scores)),
             xytext=(annotateInfo["max_index"], max(scores) + 7),
             arrowprops={'color':'red'})

plt.annotate("Min Score", 
             xy=(annotateInfo["min_index"],min(scores)),
             xytext=(annotateInfo["min_index"], min(scores) - 7),
             arrowprops={'color':'yellow'})

plt.show()








