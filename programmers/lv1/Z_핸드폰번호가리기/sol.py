# # 풀이과정
# # replace로 바꿔주기
# # 폰번호 n의 0번인덱스부터 -5번인덱스까지를 => n의 길이-4만큼 *을 쓴 것으로 

# def solution(n):
#     return n.replace(n[:-4],'*'*(len(n)-4))

# print(solution("01033334444"))
# print(solution("027778888"))


#첫 번째 풀이
def solution(phone_number):
    answer = ''
    pn = ''.join(reversed(phone_number))
    real_num = []
    num_list = []
    for _ in pn:
        num_list.append(_)
    real_num = reversed(num_list[:4])
    real_num = ''.join(real_num)
    answer = '*' * (len(phone_number)-4) + real_num

    return answer
    
print(solution('12345678901011'))
print(solution("01033334444"))
print(solution("027778888"))
print(solution('0000'))

