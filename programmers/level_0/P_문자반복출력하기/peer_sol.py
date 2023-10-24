# 풀이1
# tip: `''.join(str)` >> 문자열 결합하기. (마치 list를 append해주는 것과 같음)
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

print(solution("hello", 3))