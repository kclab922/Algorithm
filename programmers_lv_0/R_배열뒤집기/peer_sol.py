def solution(num_list):
    num_list.sort(reverse = True)
    answer = num_list
    return answer
>> 내림차순 정렬이므로, 역순과는 다름

def solution(num_list):
    num_list.reverse()
    answer = num_list
    return answer

def solution(num_list):
    return num_list[::-1]


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))