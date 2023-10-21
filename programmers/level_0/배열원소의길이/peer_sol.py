# # 풀이1
# def solution(strlist):
#     return list(map(len, strlist))

# # 풀이2
# def solution(strlist):
#     return [len(str) for str in strlist]

def solution(strlist):
    return len(strlist)


print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))