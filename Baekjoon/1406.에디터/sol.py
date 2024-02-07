from collections import deque
import sys
sys.stdin = open('input2.txt')

char = sys.stdin.readline()
n = int(sys.stdin.readline())

left = deque(char)
right = deque()
for _ in range(n):
    command = sys.stdin.readline()
    if left and command[0] == 'L':
        right.appendleft(left.pop())
    elif right and command[0] == 'R':
        left.append(right.popleft())
    elif left and command[0] == 'B':
        left.pop()
    else:
        left.append(command[2:])

left = ''.join(left).rstrip()
right = ''.join(right)
print(left+right)




