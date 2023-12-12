# 이상, 이하 매우 거슬림..
# 논문별 인용횟수가 아무리 많아도, h-index의 최댓값은 전체 논문 개수 1000개를 넘지 못함.

from collections import deque

def solution(citations):
    h_max = len(citations) # 3
    citations.sort(reverse=True) #  1 0
    citations = deque(citations)

    count = 0 # 3
    while (count != h_max):
        if citations[0] >= h_max:
            citations.popleft()
            count += 1
        else:
            h_max -= 1

    return h_max


# 다른 코드
def solution(citations):
    citations = sorted(citations) # 0 1 3 5 6
    l = len(citations) # 5
    for i in range(l): # 0 1 2 3 4
        if citations[i] >= l-i: 
            return l-i 
    return 0

print(solution([3, 0, 6, 1, 5]))