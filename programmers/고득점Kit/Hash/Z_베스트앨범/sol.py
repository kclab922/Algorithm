def solution(genres, plays):
    md = {}
    for g, p in zip(genres, enumerate(plays)):
        md[g] = sorted(md.get(g, []) + [(p)], key=lambda x: (-x[1], x[0])) 
    # '장르:(고유번호, 재생 수)' 의 리스트로 딕셔너리 생성 
    # md = {'classic': [(3, 800), (0, 500), (2, 150)], 'pop': [(4, 2500), (1, 600)]}
        
    genre = sorted(list(md.keys()), key=lambda x: -sum(i[1] for i in md[x]))
    # '장르별 재생 수의 합계'가 많은 순으로 정렬
    # genre = ['pop', 'classic']

    answer = []
    for g in genre:
        for i in range(0, 2):
            try: answer.append(md[g][i][0])
            except: pass
    # 장르별로 밸류값에서 '0번, 1번째 튜플'의 '첫 번째 값(=고유번호)'만 모아서 도출
    # answer = [4, 1, 3, 0]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))