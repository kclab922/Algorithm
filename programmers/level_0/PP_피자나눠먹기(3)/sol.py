

def solution(slice, n):
    count = 0
    if n % slice == 0:
        count = n // slice
    else:
        count = n // slice + 1
    return count

print(solution(7, 10))
print(solution(4, 12))