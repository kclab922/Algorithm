# 풀이1
# 어떻게 해서 이런 풀이가.....

def solution(slice, n):
    return ((n - 1) // slice) + 1

print(solution(7, 10))
print(solution(4, 12))