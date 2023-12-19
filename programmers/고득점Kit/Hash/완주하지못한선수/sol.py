def solution(participant, completion):
    myD = {}
    for p in participant:
        myD[p] = myD.get(p, 0) + 1
    # myD = {'leo': 1, 'kiki': 1, 'eden': 1}
    
    for c in completion:
        myD[c] -= 1
    # myD = {'leo': 1, 'kiki': 0, 'eden': 0}
    
    for k, v in myD.items():
        if v == 1:
            return k




print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
