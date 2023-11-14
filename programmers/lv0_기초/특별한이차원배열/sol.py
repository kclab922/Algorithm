# 내 코드
def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


# 다른 코드
# zip(*arr): arr의 행과 열을 서로바꿔주는 함수
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))

print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]))