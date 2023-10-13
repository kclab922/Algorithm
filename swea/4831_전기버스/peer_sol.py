import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    K, N, M = list(map(int, input().split()))  #설명에 나와있듯 첫번째는 K(1회 충전 당 이동할 수 있는거리), N(도착해야하는 위치), M(정류소 갯수)

    charge_station = list(map(int, input().split()))  #charge_station을 호출했으니 사실상 M이라는 변수는 이제 생각 안해도 될듯

    count = 0

    current = 0

    while current + K < N:  #현재위치에서 한번에 이동 가능한 K를 합한 값이 내가 도착해야하는 위치보다 클 때 루프 종료

        for move in range(K, 0, -1): #K만큼 움직이다 충전소가 있는 K-(가장 작은 수)에 충전소가 있으면 충전을 해야하니 K~0까지 -1
    
            if (current + move) in charge_station: 
                current += move                     #현재위치에서 충전소까지 이동했으니 현재 위치는 충전소이다.
                count += 1                          #충전소에서 충전을 했으면 1회 count

                break
        else:                                      #움직이는 거리 안에 충전소가 없다면 count x = 도착 x
            count = 0
            break
    
    print(f'#{tc} {count}')