def solution(num_list, n):
    result = []
    for i in range(n):
        for j in range(len(num_list)//n):
            result.append(list(num_list[i][j]))
    return result


print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))