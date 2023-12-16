# 내 코드 
# 모두 통과. but 시간복잡도 개선하고 싶음.
from collections import deque

def solution(bridge, weight, truck):
    sec = 0
    waiting = deque()
    passing = deque()
    passed = []

    # 각 트럭별로 경과시간 달아주기
    for w in truck:
        waiting.append([1, w])

    # 트럭 이동 시작
    n = len(truck)
    while len(passed) < n:
        sec += 1

        # passing
        while len(passing) and passing[0][0] == bridge:
            passed.append(passing.popleft())
            weight += passing[0][1]
        for i in range(len(passing)):
            passing[i][0] += 1
                            
        # waiting
        if (len(waiting) != 0) and (weight - waiting[0][1] >= 0):
            weight -= waiting[0][1]
            passing.append(waiting.popleft())

    return sec


# 다른 코드 (시간복잡도 최상)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0
    step = 0

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step


print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))