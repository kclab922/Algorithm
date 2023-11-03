# 내 코드 1 (list comprehension ver.)
def solution(n, numlist):
    return [m for m in numlist if m % n == 0]

# 내 코드 2
def solution(n, numlist):
    answer = []
    for m in numlist:
        if m % n == 0:
            answer.append(m)
    return answer



print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5, [1, 9, 3, 10, 13, 5]))
print(solution(12, [2, 100, 120, 600, 12, 12]))
