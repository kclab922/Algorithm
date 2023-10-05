#다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
#이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
#[입력]
#두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.
#[출력]
#첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.
#예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.
#단, 비긴 경우는 Result : Draw 라고 출력한다.

#방법1
import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

print(man1, man2)

if man1 == '가위' and man2 =='가위':
    print('Result : Draw')
elif man1 == '가위' and man2 =='바위':
    print('Result : Man2 Win!')
elif man1 == '가위' and man2 =='보':
    print('Result : Man1 Win!')
# 밑에 쭉쭉쭉 노가다...로 경우의 수 


#방법2 （구글 공유문서 엑셀 참고）
import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win')
    else:
        print('Result : Man1 Win!')



#T = int(input())
#Man1 = ['가위', '바위', '보']
#Man2 = ['가위', '바위', '보']

#for tc in range(1, T+1):
    #if Man1 == '바위' and Man2 == '가위':
        #result = (f'Result : Man{tc} win!.')
        #print(result)

