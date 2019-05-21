# -*- coding: utf-8 -*-

# import 된 모듈 내부의 요소(변수, 함수, 클래스)에
# 접근하기 위해서는 모듈명을 사용해야만 합니다.

# 만약 모듈명 자체를 사용하려고 하지 않는다면
# from 모듈명 import 변수,함수,클래스명 
# 구문을 사용해야만 합니다.

# from module_05 import num_05
# from module_05 import func_05
# from module_05 import num_05, func_05, Class_05

from module_05 import *

print(num_05)
func_05()
obj = Class_05()

# 파이썬 기본 라이브러리를 import 하는 예제
# 파이썬의 PATH로 등록된 경로에 저장되어 있어
# import 할 수 있습니다.
import csv
import sys








