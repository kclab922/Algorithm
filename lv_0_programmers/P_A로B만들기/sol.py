# 내 풀이
# 1. 기본값 = 1
# 2. 전후 길이가 다르거나 or 각 알파벳 개수가 다르면 바로 0출력하고 break
def solution(before, after):
    answer = 1
    for i in before: 
        if len(before) != len(after) or before.count(i) != after.count(i):
            answer = 0
            break                
    return answer

# 다른 풀이
# 문자열에 sort할 생각을 몬했네
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0



print(solution("olleh", "hello"))
print(solution("allpe","apple"))