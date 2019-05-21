# -*- coding: utf-8 -*-

def printMessage(msg) :
    print(f"msg -> {msg}")

# 모듈을 생성하는 경우 모듈 파일 내부에
# 실행문은 import 되는 시점에도 실행됩니다.
# 만약 모듈 내부의 실행코드가 import 되는 경우에는
# 실행하지 않기 위해서 아래와 같이 __name__ 값을
# 비교하여 처리할 수 있습니다.
# 현재 모듈 파일이 실행되는 경우(import 가 아님)
# __name__ 변수는 __main__ 값을 가집니다.
if __name__ == "__main__" :
    printMessage("Hello~ Module_03~")






