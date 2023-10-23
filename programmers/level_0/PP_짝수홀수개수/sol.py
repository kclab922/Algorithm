def solution(num_list):
    my_list = [0, 0]
    for num in num_list:
        if num % 2 == 0:
            my_list[0] += 1
        else:
            my_list[1] += 1
    return my_list

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))