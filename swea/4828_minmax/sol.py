# sort 버전
# import sys
# sys.stdin = open('input.txt')

# T = int(input()) # 첫번째 중 숫자3 받아옴. 이 숫자만큼 반복문 반복

# for tc in range(1, T+1):
#     N = int(input())

#     numbers = list(map(int, input( ).split()))

#     numbers.sort()
#     result = numbers[N-1] - numbers[0]

#     print(result)
        


# 비교 버전

# 가장 큰 숫자 담을 변수, 가장 작은 숫자 담을 변수 
# 기준점 만들어놓고, 
# 0을 기준으로 2를 비교 > 0을 지우고 2를 손에 쥠, > 

import sys
sys.stdin = open('input.txt')

T = int(input()) # 첫번째 중 숫자3 받아옴. 이 숫자만큼 반복문 반복

for tc in range(1, T+1):
    N = int(input())
    
    numbers = list(map(int, input( ).split()))

    # 비교할 때는 기준점 
    min_number = 10000000
    #min_number = numbers[0]
    max_number = 0
    #max_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number

        if max_number < number:
            max_number = number

    result = max_number -  min_number

    print(f'#{tc} {result}')

# 채점페이지에 복붙할 때는 위 두 줄 빼고. 