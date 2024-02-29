from collections import deque
import sys
sys.stdin = open('input.txt') 

TC = int(sys.stdin.readline())

q = deque()
for _ in range(TC):
    command = sys.stdin.readline()

    if 'push' in command:
        q.append(int(command[5:]))  
    elif 'pop' in command:
        print(q.popleft()) if q else print(-1)
    elif 'size' in command:
        print(len(q))
    elif 'empty' in command:
         print(0) if q else print(1)
    elif 'front' in command:
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)
     