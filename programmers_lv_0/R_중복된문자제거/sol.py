# 내 풀이
def solution(my_string):
    answer = ''
    for c in my_string:
        if c not in answer:
            answer += c
    return answer

print(solution("people"))
print(solution("We are the world"))

# 다른 풀이
# my_string 값들을 딕셔너리의 키로 만들어서 자동으로 중복 제거됨.
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

