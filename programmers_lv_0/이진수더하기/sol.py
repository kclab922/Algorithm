
def solution(bin1, bin2):
    bin1 = list(bin1)
    bin2 = list(bin2)
    answer = []
    for i in range(len(bin1)-1, -1, -1):
        if int(bin1[i]) + int(bin2[i]) == 0:
            answer = [0] + answer
        elif int(bin1[i]) + int(bin2[i]) == 1:
            answer = [1] + answer
        else:
            answer = [0] + answer
            answer[i+1] = answer[i+1] + 1

    return answer

print(solution("10", "11"))
print(solution("1001", "1111"))