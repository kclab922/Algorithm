# 내 풀이
# lower: my_string을 소문자로 변경
# sorted: 리스트로 바꾸며 abc순으로 정렬
# join: 리스트의 각 밸류값을 문자열로 합쳐서 나열
def solution(my_string):
    return ''.join(sorted(my_string.lower()))



print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))