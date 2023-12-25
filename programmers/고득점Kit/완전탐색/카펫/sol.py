def solution(brown, yellow):
    total = brown + yellow

    # total의 약수 순서쌍 (가로a, 세로b) 중 a>=b인 경우만 추출
    comb = []
    for i in range(1, int(total**0.5+1)): # range(1, 4)
        if total % i == 0:
            comb.append([total//i, i]) 
            # [[9, 1], [3, 3]]
    
    for i in range(1, int(yellow**0.5+1)):
        if yellow % i == 0:
            pass
     
    for a, b in comb:


      
       

    


    return comb

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

