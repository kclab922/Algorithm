# 계속 답은 나오는데 시간초과에 걸리는 상황 발생.

# while + slicing + pop
# def solution(ing):
#     count = 0
#     stack = []
#     while len(ing) != 0:
#         stack.append(ing.pop(0))
#         if stack[-1:-5:-1] == [1, 3, 2, 1]:
#             stack.pop()
#             stack.pop()
#             stack.pop()
#             stack.pop()
#             count += 1
#     return count





# while + pop + pop
# def solution(ing):
#     count = 0
#     stack = []
#     check = []
#     while len(ing) != 0:
#         stack.append(ing.pop(0))
#         if len(stack) >= 4:
#             check += [stack.pop()]
#             check += [stack.pop()]
#             check += [stack.pop()]
#             check += [stack.pop()]
#             if check == [1, 3, 2, 1]:
#                 count += 1
#             else:
#                 stack += [check.pop()]
#                 stack += [check.pop()]
#                 stack += [check.pop()]
#                 stack += [check.pop()]
#         check = []
#     return count






# while + indexing + pop
def solution(ing):
    count = 0
    stack = []
    while len(ing) != 0:
        stack.append(ing.pop(0))
        if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            count += 1
    return count


def solution(ing):
    count = 0
    stack = []
    num = 0
    while num < len(ing):
        num +
        if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            count += 1
    return count    

# for + indexing + pop
def solution(ing):
    count = 0
    l = []
    for i in ing:
        l += [i]
        if len(l) >= 4 and l[-1] == 1 and l[-2] == 3 and l[-3] == 2 and l[-4] == 1:
            l.pop()
            l.pop()
            l.pop()
            l.pop()
            count += 1
    return count



# for + slicing + pop
def solution(ing):
    count = 0
    l = []
    for i in ing:
        l += [i]
        if l[-1:-5:-1] == [1, 3, 2, 1]:
            l.pop()
            l.pop()
            l.pop()
            l.pop()
            count += 1
    return count



# for + pop + pop
def solution(ing):
    count = 0
    l = []
    check = []
    for i in ing:
        l += [i]
        if len(l) >= 4:
            check += [l.pop()]
            check += [l.pop()]
            check += [l.pop()]
            check += [l.pop()]
            if check == [1, 3, 2, 1]:
                count += 1
            else:
                l += [check.pop()]
                l += [check.pop()]
                l += [check.pop()]
                l += [check.pop()]
        check = []
    return count



# 결론: while문 사용이 문제였음. 




print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
