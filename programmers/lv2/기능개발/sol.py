from collections import deque

def solution(pro, spd):
    answer = []

    fin = deque()
    for p, s in zip(pro, spd):
        fin.append((100-p)//s+1 if (100-p)%s else (100-p)//s)

    while len(fin):
        n = fin[0]
        count = 0      
        if n >= fin[0]:
            fin.popleft()
            count += 1
        else: 
            answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
