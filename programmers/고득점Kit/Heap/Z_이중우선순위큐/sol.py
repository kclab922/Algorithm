import heapq as hq

def solution(operations):
    q = []
    q2 = []
    hq.heapify(q)
    hq.heapify(q2)

    for op in operations:
        if (op == 'D 1'):
            if q:
                while q:
                    hq.heappush(q2, -hq.heappop(q))
                hq.heappop(q2)
                while q2:
                    hq.heappush(q, -hq.heappop(q2))
        elif (op == 'D -1'):
            if q:
                hq.heappop(q)
        else:
            hq.heappush(q, int(op[2:]))

    return [max(q), min(q)] if q else [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))



# 질문
import heapq as hq

def solution(operations):
    q = []

    for op in operations:
        hq.heappush(q, int(op[2:]))
    return q

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# 리턴값
# [-5643, 1, -1, 16, 1, 123, -1]
# [-642, -45, 1, -1, 45, 97, 1, 653, 333]



import heapq
def solution(operations):
    answer = []
    my =[]
    heapq.heapify(my)
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(my, int(i.split()[1])) # I가 나온 경우 뒤의 숫자만 리스트에 넣기위해 띄어쓰기 기준으로 split후 리스트에 삽입
        elif i == "D -1" and len(my)!=0:
            heapq.heappop(my)
        elif i == "D 1" and len(my)!=0:
            my.pop(-1)
    my.sort()  ## my를 정렬해주었다. 근데 heappush를 사용하면 힙큐형태는 정렬이 되어나온다했는데 왜 필요한건가? 이 부분을 안넣으면 TC 6번이 통과가 안됨. 일반 리스트를 heapq.heapify()로 힙큐로 바꾸면 최소값은 [0]번째에 오는 것같음
    if len(my) != 0:
        answer.append(my[-1])
        answer.append(my[0])
    else:
        answer = [0,0]

    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
