def solution(sizes):
    # 모든 명함을 수남할 수 있는 가장 작은 지갑의 크기 return
    answer = 0
    
    # 모든 숫자 중 가장 큰 숫자를 찾고, 한 쪽 길이를 그것으로 정한다.
    # 가로세로를 변경할 수 있으므로 sort해가지고 큰 것이 맨 앞으로 오도록 한다.
    # 큰것 중에 가장 큰것, 작은 것중에 가장 큰것을 곱해서 크기로 return하면 되겠다!
    
    
    for fair in sizes:
        # 정렬함
        fair.sort()
        
    maxa = 0
    maxb = 0
    
    for a,b in sizes:
        maxa = max(a,maxa)
        maxb = max(b,maxb)
    
        
        
    return maxa * maxb