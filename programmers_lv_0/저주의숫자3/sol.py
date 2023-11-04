def new(n):
    for i in range(1, n):
        if i%3 == 0 or '3' in str(i):
            n += 1
    return n

def solution(n):
    while count > 0:
        for i in range(n+1, new(n)+1):
            if i%3 == 0 or '3' in str(i):
                count += 1


# 1~10 : 3 => 13
# 10~13: 2 => 15
# 14~15: 1 => 16
# 16~16: 0 => 16

print(count(10))