import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [list(input()) for _ in range(N)]
    
    my_list1 = []
    my_list2 = []
    result = []
 
    # 가로탐색
    for i in range(N):
        for j in range(N-M+1):
            

        for j in range(N-M+1):
            for k in range(N):


            print(f'{tc} {my_list1}')   
    #         if my_list1 == my_list1.sort(reverse=True):
    #             result = my_list1
    #         elif my_list2 == my_list2.sort(reverse=True):
    #             result = my_list2

    # print(result)



    # # 시작점 범위
    # for i in range(N-M+1):
    #     for j in range(N-M+1):

    #         # 회문 범위 설정 (가로/세로)
    #         for x in range(i+M):
    #             for y in range(j+M):

    #                 if my_list1 == my_list1.sort(reverse=True):
    #                     result = my_list1
    #                 elif my_list2 == my_list2.sort(reverse=True):
    #                     result = my_list2
            
    # print(f'#{tc} {result}')
            
