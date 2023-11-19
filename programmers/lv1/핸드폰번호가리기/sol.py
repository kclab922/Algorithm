def solution(n):
    return n.replace(n[:-4],'*'*(len(n)-4))

print(solution("01033334444"))
print(solution("027778888"))