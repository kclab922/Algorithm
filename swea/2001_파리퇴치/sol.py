import sys
sys.stdin = open('input.txt')

# input 값들 배정
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))