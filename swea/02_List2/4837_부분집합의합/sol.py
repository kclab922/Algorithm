import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))
    
    count = 0

    for i in range(1 << len(numbers)):
                    # = 1000000...(0 12개)
        temp = [] # 모든 부분집합 찾기
        for j in range(len(numbers)):
            # print(i, bin(i), bin(1<<j))
            if i & (1<<j): # 이 if문을 통과한다는 건 해당 자리에 1이 있다는 의미 
                # 여기서 T가 나온다는 건 해당 자리에 1이 있다는 것
                temp.append(numbers[j]) 
        
        if len(temp) == N and sum(temp) == K:
            count += 1

    print(f'#{tc} {count}')
