def solution(sizes):
    minSize = sizes[0]

    for i in sizes[1:]: 
        if i[0] <= minSize[0] and i[1] <= minSize[1]:
            pass
        else:
            if i[0] <= minSize[1] and i[1] <= minSize[0]:
                pass
            else:
                # 지갑사이즈 가로세로 모두에 안 들어가는 경우
                if min(i) > minSize[0] and min(i) > minSize[1]:
                    minSize = i
                # 현재 지갑사이즈 가로세로 중 하나라도 들어가는 경우
                else:
                    

            


    return minSize

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))