import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    cheese = list(map(int, input().split()))
    
    # 피자번호와 치즈번호 통일시켜주기
    pizza_info = []
    for i in range(M):
        # [1번, 7] [2번, 2], ...
        pizza_info = [i+1, cheese[i]]

        in_fire = pizza_info[:N] # 화덕에 들어간 피자
        out_fire = pizza_info[N:] # 화덕에 아직 못들어간 피자

    # 화덕에서 피자가 없어질 때까지 반복
    while in_fire:
        in_fire.pop(0) = c_i, c 

        




    
#     for i in range(1, M+1):
#         C = C_list[i-1]

#         while C == 0:
#             C = C / 2
#             if C == 0:
#                 queue.append(C)
        
#         print(queue)

#     # 1. 치즈 값을 틀에 넣는다
#     # 2. C = 0 이 될때까지 C를 반으로 줄인다 
#     # 3. C = 0 이 되면  0 in frame 이면 >> 해당 인덱스를 뽑고 새 C를 넣는다

    
   


        







# # print(f'#{tc} {last}')