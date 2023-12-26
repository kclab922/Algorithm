class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


def solution(n, wires):
    for i in range(n):
        [wires[:i]]+[wires[i+1:]]
    #     for c, d in wires[:i]+wires[i+1:]:


    return wires[:i]+wires[i+1:]

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))