# 풀이1
# 코드 이해 못함..
def solution(cipher, code):
    return cipher[code-1::code]

# 풀이2.
# tip: range 간격 설정 활용!
def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1,len(cipher),code))