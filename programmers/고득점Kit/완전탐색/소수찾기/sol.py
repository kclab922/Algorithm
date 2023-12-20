# 순열
from itertools import permutations

def solution(numbers):
    myL = []
    for i in range(len(numbers)):
        myL.append(list(permutations(numbers, i+1)))
        # myL = [[('1',), ('7',)], [('1', '7'), ('7', '1')]]

    myL2 = []
    for l in myL:
        for n in l: 
            myL2.append(int(''.join(n)))
    myL2 = list(set(myL2))
    # myL2 = [1, 71, 17, 7]

    answer = 0
    for n in myL2:
        count = 0
        for m in range(2, n):
            if n%m == 0:
                break  
            else: 
                count += 1
        if count == n-2:
            answer += 1
        
    return answer
    
print(solution('17'))
print(solution('011'))