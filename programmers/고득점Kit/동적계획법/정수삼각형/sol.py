def solution(triangle):
    answer = triangle[0][0]
    now = 0
    for i in range(1, len(triangle)):
        myMax= max(triangle[i][now], triangle[i][now+1])
        answer += myMax
        now = triangle[i].index(myMax)
    return answer

def solution(triangle):
    for yidx in range(len(triangle)):
        for xidx in range(len(triangle[yidx])):
            if yidx == 0:
                continue
            elif xidx == 0 or yidx == 1:
                triangle[yidx][xidx] += triangle[yidx-1][0]
            elif xidx == len(triangle[yidx])-1:
                triangle[yidx][xidx] += triangle[yidx-1][xidx-1]
            else:
                triangle[yidx][xidx] += max(triangle[yidx-1][xidx], triangle[yidx-1][xidx-1])
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))