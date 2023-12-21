def solution(sizes):
    minSize = sizes[0]

    for i in sizes[1:]: 
        if i[0] <= minSize[0] and i[1] <= minSize[1]:
            pass
        else:
            if i[0] <= minSize[1] and i[1] <= minSize[0]:
                pass
            else:
                minSize = sizes[i]


    return minSize

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))