import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
        
    # 10*10 격자 만들기
    matrix = [[0] * 10 for _ in range(10)]

    # 보라색 영역
    result = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                matrix[i][j] += color
                if matrix[i][j] == 3:
                    result += 1

    print(f'#{tc} {result}')

