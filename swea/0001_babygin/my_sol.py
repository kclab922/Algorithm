# babygin이면 True, 아니면 False 출력

import sys
sys.stdin = open('input.txt')

T = int(input())  # 5 가져옴

for tc in range(1, T+1):
    numbers = input()
    num_list = list(map(int, list(numbers)))
    num_list.sort()
    
    n = 0
    if num_list[n] == num_list[n+1] == num_list[n+2]:
        if num_list[n+3] == num_list[n+4] == num_list[n+5]:
            print('True')
        else:
            print('False')



    

    

    

