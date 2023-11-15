# 내 코드
# 풀이방법: tc 속 규칙 이용

def solution(N, stages):
    fail = []
    a = stages.count(1)
    b = len(stages)
    stage = 1

    while stage <= N:
        if b == 0:
            fail.append(0)
            stage += 1
        else: 
            fail.append(a/b)
            b = b-a
            a = stages.count(stage+1)
            stage += 1

    return sorted(range(1,N+1), key=lambda x: -fail[x-1])


# def solution(N, stages):
#     fail = []
#     for i in range(1, N+1):
#         not_clear = 0
#         in_stage = 0
#         for j in stages:
#             if j >= i:
#                 in_stage += 1
#                 if j == i:
#                     not_clear += 1
        
#         if in_stage == 0:
#             fail.append(0)
#         fail.append(not_clear / in_stage)

#     return sorted(range(1,N+1), key=lambda x: -fail[x-1])





print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))