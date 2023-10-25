def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += char * n
    return answer

print(solution("hello", 3))