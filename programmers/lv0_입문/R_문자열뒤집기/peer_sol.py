# 풀이1: str에서도 바로 인덱스 사용 가능!

def solution(my_string):
    return my_string[::-1]

print(solution("jaron"))
print(solution("bread"))


# 풀이2: 리스트 속 밸류값이 str인 경우 `.reverse()` 대신 `reversed()` 사용!
def solution(my_string):
    return ''.join(list(reversed(my_string)))

print(solution("jaron"))
print(solution("bread"))
