# 내 풀이
#1. .findall() 함수 이용해 숫자만 추출 => tc1) ['1', '2', '34'] 
#2. 각 원소를 int로 바꿔 sum

import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'\d+', my_string)])

# 다른 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))