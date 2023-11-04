def solution(sco, K):
    count = 0
    mixed = 0
    over_K = 0
    sco.sort()

    for n in sco:
        if n < K:
            mixed = sco[0] + sco[1]*2
            sco.pop(0)
            sco.pop(0)
            sco = [mixed] + sco 
            count += 1      
            sco.sort()        

        else:
            over_K += 1
            if over_K == len(sco):
                return count  
            else:
                continue

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))