# 풀이1
# tip: sort 함수 비교
# (1) list.sort(): 원본을 수정하나, 함수의 리턴값은 None
# (2) sorted(list): 원본을 수정하지 않고, 함수의 리턴값은 정렬된 상태

def solution(array):
    return sorted(array)[len(array)//2]

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))