# 내 풀이
# 1. s를 '공백' 기준으로 split => ['1', '2', 'Z', '3']
# 2. 일단 숫자만 골라 모두 더하기 (.isnumeric/.isdigit은 음수를 F처리하므로, !='Z'로 대체)
# 3. Z 앞자리 숫자만 빼기

def solution(s):
    answer = 0
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] != 'Z':
            answer += int(s[i])
        else:
            answer -= int(s[i-1])
    return answer


# 다른 풀이
# 내 풀이와 같은 메커니즘
# `:=`  s = s.split(" ")을 선언한 것과 같음.

def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))