def solution(n):   
    answer = []
    for num in range(1, n+1):
        if n%num == 0:
            for number in range(1, num+1):
                temp = []
                if num//number == 0:
                    temp.append(number)
                    if len(temp) <= 2:
                        answer.append(num)


    return answer

print(solution(12))
print(solution(17))
print(solution(420))