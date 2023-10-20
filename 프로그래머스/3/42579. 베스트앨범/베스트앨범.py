from collections import defaultdict

def solution(genres, plays):
    answer = []
    N = len(genres)
    musics = [[genres[i],plays[i],i] for i in range(N)]
    sort_music = sorted(musics, key=lambda x: (x[0],-x[1],x[2]))
    
    # 장르별 개수 더해서 큰 순으로 정렬
    gen = set(genres)
    gen_sum = defaultdict(list)
    for g in list(gen):
        for i in range(N):
            if g == musics[i][0]:
                gen_sum[g].append(musics[i][1])
    gen_sum = sorted(gen_sum.items(), key=lambda x : - sum(x[1]))
    gen_list = []
    for gen in gen_sum:
        gen_list.append(gen[0])
    
    # 다시구하기
    
    for g in gen_list:
        cnt = 1
        for i in range(N):
            if cnt > 2:
                break
            elif g == sort_music[i][0] and cnt <= 2:
                answer.append(sort_music[i][2])
                cnt += 1
            
    

    
    
    
    return answer