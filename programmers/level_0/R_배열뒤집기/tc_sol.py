# 방법1

# def solution(num_list):
#     answer = []
#     num_list.reverse()
#     answer = num_list
#     return answer



# 방법2 - 리뷰요망
def solution(num_list):
    answer = []

    for i in range(len(num_list)):
        answer.append(num_list[len(num_list)-1-i])    
    
    return answer


# 방법2.2 - 리뷰요망
def solution(num_list):
    answer = []

    for i in range(len(num_list)-1, 0, -1):
        answer.append(num_list[i])    
    
    return answer


# 방법3 - 리뷰요망
def solution(num_list):
    answer = []

    for num in num_list:
        answer.insert(0, num)
    
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))
