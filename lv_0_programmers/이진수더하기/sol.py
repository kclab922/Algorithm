# 내 코드 (bin함수 사용X)
# 1. 십진법으로 더하기: b1+b2를 십진법으로 더한 값을 s로 리스트화 => tc2: [2, 1, 1, 2] (str은 각 인덱스에 재할당이 안되므로 리스트화)
# 2. 이진수화: list out of range를 방지하기 위해 2단계로 나눔
#             (1) 둘쨰~끝자리가 2보다 클 때 => 2 빼서 남기고, 앞자리에 1 더하기 
#             (2) 첫째자리가 2보다 클 때 => 2 빼서 남기고, s 앞에 [1] 리스트 더하기 

def solution(b1, b2):    
    s = list(map(int, str(int(b1) + int(b2)))) 

    for i in range(len(s)-1, -1, -1):
        if i > 0:
            if s[i] >= 2:
                s[i] = s[i] - 2
                s[i-1] += 1
        else:
            if s[0] >= 2:
                s[0] = s[0] - 2
                s = [1] + s

    return ''.join([str(i) for i in s])


# 다른 코드
# int(str,2): 2진수인 str을 십진수화
# bin(int): 십진수를 이진수화 => 결과값에는 이진수를 뜻하는 '0b'가 앞에 붙어서 출력
def solution(bin1, bin2):
    return bin(int(bin1,2) + int(bin2,2))[2:]


print(solution("10", "11"))
print(solution("1001", "1111"))

