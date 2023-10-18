import sys
sys.stdin = open('input.txt')

# input 값들 배정 
T = int(input())

for tc in range(1, T+1):
    # N: 전체 보드의 길이
    # M: 파리채의 길이
    N, M = list(map(int, input().split()))

    matrix = []

    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

        
