# # 내 코드1 (tc 2개 시간초과 뜸)
# def solution(pb):
#     pb = sorted(pb, key = lambda x: len(x))

#     for i in range(len(pb)-1):
#         for k in range(i+1, len(pb)):
#             if pb[i] == pb[k][:len(pb[i])]:
#                 return False
#     return True
        

# 내 코드 
def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        if (pb[i] == pb[i+1][:len(pb[i])]) and (pb[i] != pb[i+1]):
            return False
    return True
    
# print(sorted(['1000' '110', '1102', '11']))
# ['1000', '11', '110', '1102']

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))


# 다른 코드 1
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# 다른 코드 2
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False

    return answer
