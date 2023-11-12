# 내 코드 1 (list comp.)
def solution(t, p):
    return sum([1 for i in range(len(t)-len(p)+1) if int(t[i:i+len(p)]) <= int(p)])


# 내 코드 2
def solution(t, p):
    count = 0 
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            count += 1
    return count

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))