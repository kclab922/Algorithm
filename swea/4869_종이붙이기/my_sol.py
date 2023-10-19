# N
# 10 1
# 20 3
# 30 5 = (3 + 2*1)
# 40 11 = (5 + 2*3)
# 50 21 = (11 + 2*5)

def function(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return function(N-10) + 2*function(N-20)

import sys
sys.stdin = open('input.txt')

T = int(input())
answer = 0

for tc in range(1, T+1):
    N = int(input())
    answer = function(N)

    print(f'#{tc} {answer}')


