def solution(arr):
    answer = []
    for i in range(1, len(arr)):
        while arr[i] == arr[i-1]:
            answer.remove(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))