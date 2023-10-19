def solution(citations):
    
    # 정렬 해 놓기
    citations.sort()
    maxv = max(citations)
    N = len(citations)
    maxh = 0
    for h in range(0,maxv):
        cnth = 0
        for i in range(N):
            if citations[i] >= h:
                cnth +=1
        # 센 갯수가 h보다 크다면
        if cnth >= h:
            maxh = max(h, maxh)
                

    return maxh