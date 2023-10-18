def solution(citations):
    answer = 0
    #n 편중 h번이상 인용된 논문이 h번 이상, 나머지는 h번 이하
    citations.sort()
    N = len(citations)
    # h 선택 , h이상이 h개 이상인가? 최댓값인가? 
    maxv = max(citations) + 1
    
    h_val = 0
    for n in range(0, maxv):
        cnt = 0
        for write in range(N):
            if citations[write] >= n:
                cnt += 1
        if cnt >= n:
            h_val = max(n, h_val)
            

    return h_val