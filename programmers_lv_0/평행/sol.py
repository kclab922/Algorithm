def solution(dots):
    for a in range(2):
        for b in range(4):
            for c in range(1):
                for d in range(3):
                    ????

                    if abs(int(dots[a][1]) - int(dots[c][1]) / int(dots[b][0]) - int(dots[d][0])) == abs(int(dots[x+2][1]) - int(dots[x+2][1]) / int(dots[x+3][0]) - int(dots[x+3][0])):
            
                        answer = 1
                    else:
                        answer = 0
    return answer



 for i in range(len(dots)-1):
        for j in range(i+1, len(dots)):
            line1.append(dots[i])
            line1.append(dots[j])
            
print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))