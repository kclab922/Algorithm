# 풀이1
# tip: list comprehension 할 때 for문에 if절까지 붙일 수 있구만.
def solution(n, numlist):
    return [num for num in numlist if num % n == 0]