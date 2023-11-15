# # 시간초과
# def solution(k, m, s):
#     s.sort(reverse=True)
#     answer = 0
#     while len(s) >= m:
#         answer += m*s[m-1]
#         s = s[m:]
#     return answer


# 재풀이 
# 나만 heap 썼냐 ㅡㅡ (max 580ms)
import heapq

def solution(k, m, s):
    h = []
    result = []
    answer = 0
    
    for i in s:
        heapq.heappush(h, -i)
    
    for j in range(len(h)):
        result.append(-heapq.heappop(h))

    for n in range(m-1, len(s), m):
        answer += result[n] * m

    return answer


# 다른 코드
# 쏘굿...!
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))