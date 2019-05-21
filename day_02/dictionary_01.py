# -*- coding: utf-8 -*-

# Dictionary 타입 데이터
# 특정 데이터의 검색을 위해서 사용되는 자료형
# {키 : 밸류}
program = { "lang":"python", "version":3.6 }
print(program)

# Dictionary 내부의 데이터 접근 방법
# 키 값을 활용하여 접근
# 변수명[키값]
print(program["lang"])
print(program["version"])

# Dictionary 에 데이터를 추가하는 방법
# 변수명[newKey] = newValue
program["level"] = "high"
print(program)







