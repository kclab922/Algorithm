def solution(participant, completion):
    d = {}
    for p in participant:
        d[p] = d.get(p, 0) + 1
    
    return d




print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
