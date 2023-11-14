def solution(c1, c2, goal):
    l1 = []
    l2 = []
    for g in goal:
        if g in c1:
            l1 += [g]
        else:
            l2 += [g]
    if len(goal)==len(c1)+len(c2) and l1 == c1 and l2 == c2:
        return 'Yes'
    else: 
        return 'No'

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))