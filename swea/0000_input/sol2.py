# 2차원 리스트 입력

import sys
sys.stdin = open('input2.txt') 

N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)

    

# # 데이터 자체를 반복. item 자체를 활용하는 방법
# for row in matrix:
#     for item in row:
#         print(item)

# index 접근1 (행 우선 반복. 맨 윗줄부터 가로로 왼>오로)
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        print(row, col, matrix[row][col])

# index 접근2 (열 우선 반복. 맨 왼쪽줄부터 오른쪽으로 세로로)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(j, i, matrix[j][i])
