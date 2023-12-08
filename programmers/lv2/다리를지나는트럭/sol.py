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
        for i in range(len(passing)):
            passing[i][0] += 1
                
        # waiting
        if (len(waiting) != 0):
            sum_w = 0
            for _, w in passing:
                sum_w += w
            if sum_w + waiting[0][1] <= weight:
                passing.append(waiting.popleft())

    return sec

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))