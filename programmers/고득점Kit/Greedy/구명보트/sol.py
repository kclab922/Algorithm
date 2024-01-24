# 정확성테스트 전부 통과 / 효율성테스트 모두 시간초과
# def solution(people, limit):
#     answer = 0
#     people.sort() 

#     while people:
#         saved = people.pop() 
#         answer += 1

#         for person in people:
#             if person + saved <= limit:
#                 people.remove(person)
#                 break
        
#     return answer


# 답은 모두 맞으나, 시간초과 
# def solution(people, limit):
#     answer = 0
#     people.sort() # 50 50 70 

#     while people:
#         saved = people.pop() # 80
#         print(saved)
#         answer += 1

#         count = 0 # 1
#         while count < len(people): # 3
#             if people[-1] + saved <= limit:
#                 people.pop()
#                 break
#             else:
#                 people = [people.pop()] + people
#                 count += 1

#         people.sort()
        
#     return answer




# from collections import deque
# def solution(people, limit):
#     boat = 0
#     people = deque(sorted(people))

#     while people:
#         saved = people.pop()
#         boat += 1

#         if (people) and (saved + people[0] <= limit):
#             people.popleft()

#     return boat


from collections import deque
def solution(people, limit):
    boat = 0
    people = deque(sorted(people))

    while people:
        if len(people) == 1:
            return boat + 1
        else:
            if (people.pop() + people[0] <= limit):
                people.popleft()
            boat += 1

    return boat

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))