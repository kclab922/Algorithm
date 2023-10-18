import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N, K = list(map(int, input().split()))

    A = [i for i in range(1, 13)]
    result = 0

    for i in range(1<<12):
        temp = [] # 모든 부분집합 찾기
        sum_sub = 0
        for j in range(12):
            # print(i, bin(i), bin(1<<j))
            if i & (1<<j):
                # 여기서 T가 나온다는 건 해당 자리에 1이 있다는 것
                sum_sub += A[j]
                temp.append(A[j]) 
        
        
        if len(temp) == N and sum_sub == K:
            result += 1

    print(f'#{tc} {result}')
