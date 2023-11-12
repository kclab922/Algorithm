def solution(n):
    b3 = []
    while n//3 != 0:
        a,b = divmod(n, 3)
        b3 += [b] 
        n = a
    b3 = ''.join(list(map(str, b3+[a])))
    return int(b3, 3)


print(solution(45))
print(solution(125))