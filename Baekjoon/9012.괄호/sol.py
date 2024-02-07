from collections import deque
import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    s = sys.stdin.readline().split()
    

    print(s)
    while s:
        stack.append(s.pop())
        if stack[-2:] == [')', '(']:
            stack.pop()
            stack.pop()
    # print('NO') if stack else print('YES')