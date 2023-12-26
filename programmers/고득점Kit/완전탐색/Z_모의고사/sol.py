def solution(answers):
    p1 = [1, 2, 3, 4, 5] * (10000//5)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000//8+1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000//10)
    l = len(answers)

    score = [0, 0, 0]
    for answer, p1, p2, p3 in zip(answers, p1[:l], p2[:l], p3[:l]):
        if p1 == answer: score[0] += 1
        if p2 == answer: score[1] += 1
        if p3 == answer: score[2] += 1

    answer = []
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))