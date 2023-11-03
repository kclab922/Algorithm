

def solution(b1, b2):
    b1 = [int(n) for n in list(b1)]
    b2 = [int(n) for n in list(b2)]
    result = [0 for _ in range(len(b1)+1)]

    for i in range(len(b1)-1, -1, -1):
        if b1[i] + b2[i] + result[i+1] < 2:
            result[i+1] = b1[i] + b2[i] + result[i+1]
        elif b1[i] + b2[i] + result[i+1] == 2:
            result[i+1] = 0
            result[i] += 1
        else:
            result[i+1] = 1
            result[i] += 1

    return ''.join([str(n) for n in result])


print(solution("10", "11"))
print(solution("1001", "1111"))
