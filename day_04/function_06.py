# -*- coding: utf-8 -*-

# 다수개의 정수 값을 매개변수로 입력받아
# 총 합계를 구하는 함수를 작성
# (전달되는 개수는 고정되지 않음)

# 매개변수가 정해지지 않은 경우 처리하는 방법
# (매개변수가 고정되어 있지 않은 경우)

# 매개변수의 이름에 * 를 사용하는 경우
# 개수가 고정되지 않은 매개변수가 됩니다.
# 이러한 경우 반복문을 활용하여 처리할 수 있음

def total( *num ) :
    sumValue = 0
    
    for n in num :
        sumValue += n
        
    return sumValue

# 매개변수 num은 고정되어 있지 않기 때문에
# 전달하지 않아도 실행에 에러가 없습니다.
sum_0 = total()
print(f"sum_0 -> {sum_0}")

sum_1 = total(10,20,30)
print(f"sum_1 -> {sum_1}")

sum_2 = total(10,20,30,40,50,60,70,80,90,100)
print(f"sum_2 -> {sum_2}")













