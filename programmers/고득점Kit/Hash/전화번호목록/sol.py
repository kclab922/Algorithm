# # 내 코드1 (tc 2개 시간초과 뜸)
# def solution(pb):
#     pb = sorted(pb, key = lambda x: len(x))

#     for i in range(len(pb)-1):
#         for k in range(i+1, len(pb)):
#             if pb[i] == pb[k][:len(pb[i])]:
#                 return False
#     return True
        

# 내 코드 2
def solution(pb):
    myD = {}
    for i in pb:
        myD[i] = myD.get(i, 0)

    for k in pb.keys():
        
    
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))