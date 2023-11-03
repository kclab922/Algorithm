def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split(' ') # ['5', '+', '6', '=', '11']
        cal = int(q[0])
        for c in q:
            if c == '+':
                cal += int(q[q.index(c) + 1])
            elif c == '-':
                cal -= int(q[q.index(c) + 1])
        if cal == int(q[-1]):
            answer.append('O')
        else:
            answer.append('X')
                
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))