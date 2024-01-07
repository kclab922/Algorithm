from itertools import product

def solution(numbers, target):
    myL = []
    for n in numbers:
        myL.append((n, -n))
    # [(4, -4), (1, -1), (2, -2), (1, -1)]

    count = 0
    for k in list(product(*myL)):
        if sum(k) == target:
            count += 1
    # [(4, 1, 2, 1), (4, 1, 2, -1), (4, 1, -2, 1)....

    return count
    



print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))