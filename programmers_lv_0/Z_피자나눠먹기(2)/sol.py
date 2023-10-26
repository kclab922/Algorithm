# 내 풀이
def solution(n):
    # n=100명) 100명이 1조각씩 먹는 경우 >> 100과 6의 최소공배수는 300 >> 50판 필요
    for num in range(1, 51):
        if 6*num % n == 0:
            return num



print(solution(6))
print(solution(10))
print(solution(4))