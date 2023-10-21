# 풀이1
# 이해값1. map(function, iterable)
#         : iterable이 리스트인 경우, 리스트의 각 밸류값에 function 적용
def solution(strlist):
    return list(map(len, strlist))

# 풀이2
# 요건 생각 못했네,,,, 
def solution(strlist):
    return [len(str) for str in strlist]


print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))