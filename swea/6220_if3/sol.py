import sys
sys.stdin = open('input.txt')

T = int(input())
# 대문자 T : 전체 테스트케이스의 개수 - 첫째줄

# for test_case in range(TC):
# TC가 0부터 시작해서 0, 1 들어감. 
# 1부터 시작하도록 맞춰주려면 아래처럼

# i는 1부터 시작하는 것으로. 
# 소문자 tc는 값.
for tc in range(1, T+1):
    char = input()
    if char.islower():
        print(f'#{tc} {char} 는 소문자 입니다.')
    else:
        print(f'#{tc} {char} 는 대문자 입니다.')
