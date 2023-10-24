def solution(n):
    my_sum = 0
    for num in str(n):
        my_sum += int(num)
    return my_sum

print(solution(1234))
print(solution(930211))



