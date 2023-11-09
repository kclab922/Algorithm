# 풀이1: 리스트를 문자열로 바꿀 때는 `''.join()` 사용!
def solution(my_string):
    return ''.join(list(my_string)[::-1])

print(solution("jaron"))
print(solution("bread"))