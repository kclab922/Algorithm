import sys
sys.stdin = open('input.txt')

n = int(input())

# 풀이1: 프린트문에 기냥 써도 됨... for문 반복 기준으로 줄 바뀜.
for i in range(1, n+1):
    print('*'*i)
