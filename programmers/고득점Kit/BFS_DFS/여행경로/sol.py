def solution(tickets):

    queue = deque()
    visited = [0] * len(tickets)
    
    while queue:
        
   