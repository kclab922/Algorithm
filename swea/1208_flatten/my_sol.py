import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):

    total_flatten = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    min = numbers[0]
    max = numbers[len(numbers)-1]
    difference = max - min
    
   
    for difference in range(1, total_flatten+1):
        while difference <= 1:
            numbers.sort()
            difference = max - min
            
        break

    print(f'#{tc} {difference}')
