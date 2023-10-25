import sys
sys.stdin = open('input.txt')

n = int(input())

# 내 풀이1.
for i in range(1, n+1):
    print(''.join('*'*i))
