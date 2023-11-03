# 내 풀이1 (short.ver)
def solution(my_string, n):
    return ''.join([char*n for char in my_string])

# 내 풀이2
def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += char * n
    return answer

print(solution("hello", 3))