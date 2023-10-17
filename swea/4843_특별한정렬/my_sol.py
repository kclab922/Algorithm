import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)

    for i in range(1, ??):
        numbers[2*i-1] = numbers[N-i]
        


    

