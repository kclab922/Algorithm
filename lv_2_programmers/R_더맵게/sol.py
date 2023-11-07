from heapq import heappush, heappop, heapify

def solution(sco, K):
    heapify(sco)
    count = 0

    while sco[0] < K:
        heappush(sco, heappop(sco)+heappop(sco)*2)
        count += 1

        if len(sco) == 1 and sco[0] < K:
            return -1
    
    return count




print(solution([1, 2, 3, 9, 10, 12], 7))