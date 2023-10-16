import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = list(map(int, input().split()))

for tc in (1, T+1):
    matrix = []
    matrix.append(numbers)

    print(matrix)
        