# 내 코드 1
def solution(k, s):
    answer = []
    for i in range(len(s)):
        if i < k:
            answer += [min(s[:i+1])]
        else:
            answer += [sorted(s[:i+1], reverse=True)[k-1]]
    return answer



# 내 코드 2
import heapq 




print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))