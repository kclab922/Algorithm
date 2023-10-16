import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc = int(input())

    matrix = []

    # i, j, a 반복문을 돌리는 변수 지정
    # _ => 변수를 활용하지 않을 예정
    for _ in range(100):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    max_total = 0
    
    # 가로줄 반복
    for row in range(100):
        total = 0
        # 세로줄 반복
        for col in range(100):
           # 첫번째 줄의 합
           total += matrix[row][col]
        if max_total < total:
            max_total = total

    # 세로줄 반복    
    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]
        if max_total < total:
            max_total = total
    

    # 좌상단-우하단 대각선
    for i in range(100):
        total = 0
        total += matrix[i][i] 
    if max_total < total:
        max_total = total

    # 우상단-좌하단 대각선
    for i in range(100):
        total = 0
        total += matrix[i][99-i]
    if max_total < total:
        max_total = total

    print(max_total)






