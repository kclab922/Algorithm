# 내 코드 1 (list comp. ver)
def solution(arr, c):
    return [sorted(arr[i[0]-1:i[1]])[i[2]-1] for i in c]


# 내 코드 2
def solution(arr, c):
    answer = []
    for i in c:
        answer += [sorted(arr[i[0]-1:i[1]])[i[2]-1]]
    return answer


# 다른 코드 1
# 이게 제일 좋다. 'a,b,c'로 for문 돌릴 수 있음을 참고.
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]


# 다른 코드 2
# 람다 아직도.,,,
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))