import sys
sys.stdin = open('input.txt')

# input 값들 배정
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 최댓값 설정
    max_kill = 0

    # 타격박스 왼쪽 위 기준 (0,0)부터 (N-M, N-M)까지 검토
    for a in range(N-M+1):
        for b in range(N-M+1):
            
            # 타격박스 M X M 만들고 합계 구하기 
            sum_box = 0
            for c in range(a, a+M):
                for d in range(b, b+M):
                    sum_box += matrix[c][d]
            
            # 합의 최댓값 도출
            if max_kill < sum_box:
                max_kill = sum_box

    print(f'#{tc} {max_kill}')








