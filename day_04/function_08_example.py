# -*- coding: utf-8 -*-

# range 함수와 동일하게 동작하는
# range_custom 함수를 작성하세요.
def range_custom(*stop) :
    return_list = []
    
    if len(stop) == 0 :
        return None
    
    start = 0
    step = 1    
    end = stop[0]
    if len(stop) == 2 :
        start = stop[0]
        end = stop[1]
    elif len(stop) == 3 :
        start = stop[0]
        end = stop[1]
        step = stop[2]
        
    while start < end :
        return_list.append(start)
        start += step
    
    return return_list

print(range_custom(10))
print(range_custom(5, 10))
print(range_custom(5, 10, 2))

print(range_custom())

for i in range_custom(10) :
    print(i)






