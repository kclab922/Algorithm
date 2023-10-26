def solution(n):
    count = 0
    for i in range(1, n+1):
        a, b = divmod(n, i)
        if b == 0:
            count += 1
        if a * b == n:
            count -= 1

    return count