def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0) 
        if any(cur[1] < q[1] for q in queue):
           # all(~~)
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# from string import ascii_uppercase
# from collections import deque

# def solution(priorities, location):
#     answer = 0
#     Alpha_list = list(ascii_uppercase)
#     AL_list = deque([Alpha_list[i] for i in range(len(priorities))]) # deque(['A', 'B', 'C', 'D'])
#     my_priorities = deque(priorities) # deque([2, 1, 3, 2])
#     check = dict(zip(AL_list, priorities)) # {'A': 2, 'B': 1, 'C': 3, 'D': 2}
#     my = AL_list[location] # C
#     final = []

#     while my_priorities:
#         max_priority = max(my_priorities)

#         while check[AL_list[0]] != max_priority:
#             AL_list.append(AL_list.popleft())
#             my_priorities.append(my_priorities.popleft())

#         final.append(AL_list.popleft())
#         my_priorities.popleft()
        
#     answer = final.index(my) + 1

#     return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([5, 4, 3, 2, 1], 0))
print(solution([2,3,3,2,9,3,3], 3))