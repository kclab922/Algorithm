def solution(bin1, bin2):
    s = list(int(bin1) + int(bin2))
    # result = ''
    # for i in range(len(s)-2, -1, -1):
    #     if s[i] == '2':
    #         s[i] = '0'
                
    return s



print(solution("10", "11"))
print(solution("1001", "1111"))
