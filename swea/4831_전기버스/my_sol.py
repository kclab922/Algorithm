# # K: 한 번 충전으로 최대 이동 가능한 정류장의 수
# # N: 총 정류장의 개수
# # M: 충전기의 개수
# # charge_stops: 충전기를 설치한 정류장 번호
# # 조건: 1 <= K, M, N <= 100
# # 조건: 1 <= T <= 50

# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for tc in range(1, T+1):

#     numbers = list(map(int, input().split()))
#     charge_stops = list(map(int, input().split()))
#     K = numbers[0]
#     N = numbers[1]
#     M = numbers[2]

#     minimum_charge = 0
#     now = 0
#     now <= N

#     for idx in range(len(charge_stops)):
#         idx = 0
#         if K < int(charge_stops[1]):
#             now = int(charge_stops[0])
#             if K < int(charge_stops[0]):
#                 minimum_charge = 0
#         elif K >= int(charge_stops[1]):
#             minimum_charge = 0
        
#     # if K >= int(charge_stops[0]):
#     #     now = int(charge_stops[0])
#     #     minimum_charge += 1

#     # if K < int
#     # else:
#     #     minimum_charge = 0

#     # if int

# print(f'#{tc} {minimum_charge}')








# charge_stops: 충전기를 설치한 정류장 번호
# 조건: 1 <= K, M, N <= 100
# 조건: 1 <= T <= 50

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K: 최대로 이동 가능한 정류장의 수
    # N: 종점
    # M: 충전기가 설치된 정류장 개수

    K, N, M = list(map(int, input().split()))

    bus_stops = list(map(int, input().split()))

    count = 0
    now = 0


    while now < N:
        # 현재 위치를 기준으로 최대로 갈 수 있는 범위를 찾은 후 
        # 첫번쨰로 만나는 충전소에서 충전하고 넘어가기
        # 한 칸씩 뒤로 넘어오다가 
        for i in range(now+K, now, -1):
            # 1. 최대범위가 종점을 넘는 경우
            if i >= N:
                now = N
                break # 더이상 앞으로 갈 필요가 없음.
            # 2. 최대범위가 아직 종점을 넘지 않는 경우
            if i in bus_stops:
                now = i 
                count += 1
                break
        # 앞으로 계속 갔는데 충전소가 없다면? => 도착 불가능한 상태    
        else:  # 이 else는 for문이 끝까지 다 돌았음에도 break를 안 만나면(break 안 만남) 실행
            count = 0
            now = N  # while문을 끝내는 코드


    print(f'#{tc} {count}')