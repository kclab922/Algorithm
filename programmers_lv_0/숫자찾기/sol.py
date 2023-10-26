# 내 풀이
def solution(num, k):
    answer = 0
    for num in list(str(num)):
        if k in num:
            answer = list(str(num)).index(k) + 1
    return answer

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))