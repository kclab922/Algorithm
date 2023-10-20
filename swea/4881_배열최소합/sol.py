# 1. N개의 숫자를 규칙대로 골라 그 셋을 더한 값을 고른다.
# 2. 그들 중 최솟값만 남게 한다.


import sys
sys.stdin = open('input.txt')

T = int(input())
min_sum = 100000000

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)
    
        N_sum = 0
        for _ in range(N):
            for x in range(N):
                for y in range(N):
                    if matrix[x][y]
            

    
