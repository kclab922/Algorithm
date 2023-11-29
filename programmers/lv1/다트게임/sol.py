def solution(dart):
    dartSTR = ''
    for i in dart:
        dartSTR += i if i.isdigit() else i + ' '
        dart = dartSTR.split()
    # dartSTR = '1D # 2S * 3S'
    # dart = ['1D', '#', '2S', '*', '3S']
    
    area = {'S':1, 'D':2, 'T':3}
    for i in range(len(dart)):
        if dart[i][-1] in area.keys():
            dart[i] = int(dart[i][:-1]) ** area[dart[i][-1]]
        elif dart[i] == '#':
            dart[i-1] = dart[i-1] * (-1)
        elif dart[i] == '*':
            if i == 1:
                dart[i-1] = dart[i-1] * 2
            else: 
                dart[i-1] = dart[i-1] * 2
                if str(dart[i-2]).isdigit():
                    dart[i-2] = dart[i-2] * 2
                else:
                    dart[i-3] = dart[i-3] * 2
    # dart = [-2, '#', 4, '*', 3] (연산완료)

    return sum([i for i in dart if i not in ['#', '*']])
    # 숫자만 뽑아서 더하기


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))