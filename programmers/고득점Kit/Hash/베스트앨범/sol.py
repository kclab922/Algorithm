def solution(genres, plays):
    md = {}
    for g, p in zip(genres, enumerate(plays)):
        md[g] = sorted(md.get(g, []) + [(p)], key=lambda x: (-x[1], x[0])) 
    # md = {'classic': [(3, 800), (0, 500), (2, 150)], 'pop': [(4, 2500), (1, 600)]}
        
    count_play = []
    for k in md.keys():
        count_play.append((k, sum(list(map(lambda x: x[1], md[k])))))
    count_play.sort(key=lambda x: -x[1])
    # count_play = [('pop', 3100), ('classic', 1450)]

    answer = []
    for c in count_play:
        for k in range(0, 2):
            try: answer.append(md[c[0]][k][0])
            except: pass # 장르의 원소가 1개인 경우

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))