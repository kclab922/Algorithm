# 내 풀이
# dots에 sort => [[1, 1], [1, 2], [2, 1], [2, 2]]
# (리스트 상)오른쪽 끝 점 - 왼쪽 끝 점 == (그래프 상)우측상단 점 - 좌측하단 점

def solution(dots):
    d = sorted(dots)
    return (d[3][0] - d[0][0]) * (d[3][1] - d[0][1])
    

# 다른 풀이
# print(solution([[1, 2], [3, 4], [5, 6], [7, 8]])) 
# return (max(dots)[0], min(dots)[0], max(dots)[1], min(dots)[1]) => (7, 1, 8, 2)
#         0열 최댓값,    0열 최솟값,    1열 최댓값,   1열 최솟값
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))
