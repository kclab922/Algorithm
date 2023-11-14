# 내 코드 1 (시간 너무 길어..)
def solution(k, s):
    answer = []
    for i in range(len(s)):
        if i < k:
            answer += [min(s[:i+1])]
        else:
            answer += [sorted(s[:i+1], reverse=True)[k-1]]
    return answer



# 다른 코드 1
# 좋다 이 코드
def solution(k, score):
    q = []
    answer = []

    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))

        answer.append(min(q))

    return answer


# 다른 코드 2
# 다시보자 지금 머리 뜨거움
import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer



print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))