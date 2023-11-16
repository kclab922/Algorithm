import sys
sys.stdin = open('input.txt')


# 내 코드
n,m = map(int, input().split())
for _ in range(m):
    print('*' * n)


# 다른 코드
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)