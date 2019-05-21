# -*- coding: utf-8 -*-

# 함수의 매개변수 선언 시, 기본값을 지정하는 방법

# def 함수명(매개변수명 = 기본값)
# 기본값이 지정된 매개변수는 함수의 호출 시,
# 값을 전달하지 않아도 정상적으로 실행될 수 있습니다.
# (기본값을 사용하여 실행)
def calculator(n1, n2, operator="+") :    
    result = n1
    
    if operator == "+":
        result += n2
    elif operator == "-":
        result -= n2
    elif operator == "*":
        result *= n2
    elif operator == "/":
        result /= n2
    elif operator == "%":
        result %= n2
    
    return result

r = calculator(15, 10)
print(f"r -> {r}")
r = calculator(15, 10, "-")
print(f"r -> {r}")
r = calculator(15, 10, "*")
print(f"r -> {r}")
r = calculator(15, 10, "/")
print(f"r -> {r}")
r = calculator(15, 10, "%")
print(f"r -> {r}")
