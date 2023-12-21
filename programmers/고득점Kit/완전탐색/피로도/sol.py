from itertools import permutations

def solution(k, d):
    for i in range(len(d), 1, -1):
        for j in permutations(d, i): # list = [([80, 20], [50, 40], [30, 10]), ([80, 20], [30, 10], [50, 40]), ... ]
            k2 = k
            count = 0
            for n in j: # j = ([80, 20], [50, 40], [30, 10])
                if k2 >= n[0]:
                    k2 -= n[1]
                    count += 1
                else:
                    break
            if count == len(j):
                return len(j)
    return 0



print(solution(80, [[80,20],[50,40],[30,10]]))