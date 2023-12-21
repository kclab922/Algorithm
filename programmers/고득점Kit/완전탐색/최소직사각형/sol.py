# 내 코드 1
# 각 명함의 가로/세로 중 작은 값들을 모아서 그것들 중 최댓값 * 각 명함의 가로/세로 중 큰 값들을 모아서 그것들 중 최댓값
def solution(sizes):
    return max([sorted(size)[0] for size in sizes]) * max([sorted(size)[1] for size in sizes])

# 내 코드 2
def solution(sizes):
    size = sorted(sizes[0])

    for i in sizes[1:]: 
        if min(i) > size[0]:
            size[0] = min(i)
        if max(i) > size[1]:
            size[1] = max(i)

    return size[0] * size[1]







print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))