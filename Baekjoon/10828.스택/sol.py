import sys
sys.stdin = open('input.txt') 

TC = int(sys.stdin.readline())

stack = []
for tc in range(TC):
    command = sys.stdin.readline()

    if 'push' in command:
        stack.append(int(command[5:]))
    elif 'pop' in command:
        print(stack.pop()) if stack else print(-1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
         print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)

        

    # myD = {
    # 'push': stack.append(int(command[1])) if ,
    # 'pop': print(stack.pop()) if stack else print(-1),
    # 'size' : print(len(stack)),
    # 'empty' : print(0) if stack else print(1),
    # 'top': print(stack[-1]) if stack else print(-1)
    # }
    
    # myD[command[0]]




