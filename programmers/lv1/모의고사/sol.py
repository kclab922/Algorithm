def solution(a):
    p1 = [1, 2, 3, 4, 5] * (len(a)//5+1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(a)//8+1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(a)//10+1)
    score = [0, 0, 0]

    for i in range(len(a)):
        if a[i] == p1[i]:
            score[0] += 1
        if a[i] == p2[i]:
            score[1] += 1
        if a[i] == p3[i]:
            score[2] += 1

    if score.count(max(score)) == 1:
        return [score.index(max(score)) + 1]
    elif score.count(max(score)) == 2:
        return [1, 2, 3].remove(score.index(min(score))+1)
    else:
        return [1, 2, 3]
        
    


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))