# 내 코드
def solution(dart):
    dartCUT = ''
    for i in dart:
        dartCUT += i if i.isdigit() else i + ' '
        dart = dartCUT.split()
    # dartCUT = '1D # 2S * 3S'
    # dart = ['1D', '#', '2S', '*', '3S']
    
    area = {'S':1, 'D':2, 'T':3}
    for i in range(len(dart)):
        if dart[i][-1] in area.keys():
            dart[i] = int(dart[i][:-1]) ** area[dart[i][-1]]
        elif dart[i] == '#':
            dart[i-1] = dart[i-1] * (-1)
        elif dart[i] == '*':
            dart[i-1] = dart[i-1] * 2
            if i != 1:
                if str(dart[i-2]).isdigit():
                    dart[i-2] = dart[i-2] * 2
                else:
                    dart[i-3] = dart[i-3] * 2
    # dart = [-2, '#', 4, '*', 3] (연산완료)

    return sum([i for i in dart if i not in ['#', '*']])
    # 숫자만 뽑아서 더하기


# 다른 코드
# 나와 같은 풀이과정은 비슷
# 1. for문 돌릴 때 '10'이 분리될까봐 10->k 이용 / list.comp 형태 참고
# 2. dart에 계속 재할당한 나와 달리, 여분의 리스트 answer을 만들어 연산이 비교적 단순화됨
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    # point = ['1', 'D', '#', '2', 'S', '*', '3', 'S']

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))