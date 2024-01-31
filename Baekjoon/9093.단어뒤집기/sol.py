import sys
sys.stdin = open('input.txt') 

TC = int(input())

for tc in range(TC):
    answer = ''
    words = input().split()
    for word in words:
        answer += word[::-1] + ' '
    print(answer)


