def solution(data, ext, v_ext, srt):
    answer = []
    extD = {"code":0, "date":1, "maximum":2, "remain":3}
    
    dataD = {}
    for i, d in enumerate(data):
        dataD[i] = d

    for i in range(len(data)):
        if data[i][extD[ext]] < v_ext:
            answer.append(data[i])

    return sorted(answer, key = lambda x: x[extD[srt]])

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))