# 내 풀이
# common이 최소 3개 이상임을 이용
# 1. 등차수열([0]-[1] = [1]-[2])이면 => [-1] + 공차
# 2. 아니면 => 등비수열이므로 => [-1] * 공비

def solution(c):
    return c[-1] + (c[1]-c[0]) if c[0] - c[1] == c[1] - c[2] else int(c[-1] * (c[1]/c[0]))


print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
