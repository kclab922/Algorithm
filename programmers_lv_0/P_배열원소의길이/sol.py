# 풀이1
def solution(strlist):
    length = []
    for i in range(len(strlist)):
        length.append(len(strlist[i]))
    return length

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))