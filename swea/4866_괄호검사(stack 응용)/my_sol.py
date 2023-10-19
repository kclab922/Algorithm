import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    letters = input()
    targets = ''
    result = ''

    # 1. input data에서 괄호들만 빼내어 string 만들기
    for char in letters:
        if char == '(' or char == ')' or char == '{' or char == '}':
            targets += char
    
    # 2. 짝수개인지 확인 > 홀수면 일단 짝 안맞는 것이므로 0
    if len(targets) % 2 == 1:
        result = '0'

    # 3. 짝수개면? > }) 포함하면 잘못된 짝이므로 0
    else: 
        if '})' in targets:
            result = '0'
        else:
            result = '1'

    print(f'#{tc} {result}')