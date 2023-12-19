def solution(pb):
    pb = sorted(pb, key = lambda x: len(x))

    for i in range(len(pb)-1):
        if pb[i] in pb[i+1][]:
            return False
    return True
        

print(solution(["119", "97674223", "1195524421"]))