
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

    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0

    # 충전을 하면서 지나가야 하는 경우
    else:
        # 문제의 목표: 내가 갈수있는 최대거리와 가장 가까이 있는 정류장에서 충전하기
        
        # 버스가 아직 종점에 도착하지 않았다면 계속 반복해라!
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