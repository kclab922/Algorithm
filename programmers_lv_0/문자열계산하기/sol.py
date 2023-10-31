# s내 풀이 (정확성 50)
def solution(my_string):
    ms = my_string.split()
    answer = int(ms[0])
    for c in ms:
        if c == '+':
            answer += int(ms[ms.index(c)+1])
        elif c == '-':
            answer -= int(ms[ms.index(c)+1])
            
    return answer

print(solution('3 + 4'))