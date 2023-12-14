import heapq as hq

def solution(operations):
    q = []
    q2 = []
    hq.heapify(q)
    hq.heapify(q2)

    for op in operations:
        if (op == 'D 1'):
            if q:
                while q:
                    hq.heappush(q2, -hq.heappop(q))
                hq.heappop(q2)
                while q2:
                    hq.heappush(q, -hq.heappop(q2))
        elif (op == 'D -1'):
            if q:
                hq.heappop(q)
        else:
            hq.heappush(q, int(op[2:]))

    return [max(q), min(q)] if q else [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))



# 질문
import heapq as hq

def solution(operations):
    q = []

    for op in operations:
        hq.heappush(q, int(op[2:]))
    return q

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# 리턴값
# 의문사항: heappush를 하는데, 왜 오름차순 정렬이 안 된 리스트가 출력되는가?
# [-5643, 1, -1, 16, 1, 123, -1]
# [-642, -45, 1, -1, 45, 97, 1, 653, 333]