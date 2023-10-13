# import sys
# sys.stdin = open('input.txt')

# T = int(input()) # 첫번째 중 숫자3 받아옴. 이 숫자만큼 반복문 반복

# for tc in range(1, T+1):
#     N = int(input())

#     numbers = list(map(int, input( ).split()))

#     numbers.sort()
#     result = numbers[N-1] - numbers[0]

#     print(result)
        


import sys
sys.stdin = open('input.txt')

T = int(input()) # 첫번째 중 숫자3 받아옴. 이 숫자만큼 반복문 반복

for tc in range(1, T+1):
    N = int(input())


    numbers = list(map(int, input( ).split()))

    for i in range(1, N+1):
        if numbers[i]  
        


    # result = max_num - min_num



# 가장 큰 숫자 담을 변수, 가장 작은 숫자 담을 변수 
# 기준점 만들어놓고, 
# 0을 기준으로 2를 비교 > 0을 지우고 2를 손에 쥠, > 