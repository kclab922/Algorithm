def solution(tickets):
    answer = []

    routes = {}
    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]
    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    for r in routes.keys():
        routes[r].sort(reverse = True)
    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}
    # 역순 정렬: 이후 pop 사용 목적

    stack = ["ICN"]
    while stack:
        top = stack[-1]  # ICN
        # 스택 top을 start로 하는 티켓이 없는 경우
        if (top not in routes) or (not routes[top]):
            answer.append(stack.pop())   # top을 스택에서 꺼내서 answer에 저장
        # 스택 top을 start로 하는 티켓이 있는 경우
        else:
            stack.append(routes[top].pop())
    # answer = ['SFO', 'ATL', 'SFO', 'ICN', 'ATL', 'ICN']

    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))