def solution(people, limit):
    
    while people:
        people.sort()
        person = people.pop()
        if person + people[-1] <= limit:
            



print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))