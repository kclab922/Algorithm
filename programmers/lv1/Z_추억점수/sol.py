# 내 코드
def solution(n, y, p):
    answer = []
    for i in p:
        count = 0
        for j in i:
            if j in n:
                count += y[n.index(j)]
        answer.append(count)
    return answer


# 다른 코드
# 똑같은 풀이를 list comp.로
def solution(이름, 점수, 사진)
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]



print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))