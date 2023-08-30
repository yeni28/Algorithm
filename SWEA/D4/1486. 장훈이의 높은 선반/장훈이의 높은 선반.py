#인덱스와 합을 넘겨준다.
def dfs(n, nsum):
    global min_value
    # 합이 최솟값을 넘을 시
    if nsum >= min_value:
        #계산하지 않는다.
        return
    #마지막 인덱스까지 다 확인했다면,
    if n >= N:
        # 그 합이 선반보다 큰지 확인한다.
        if nsum >= B:
            min_value = nsum
        return
    v[n] = 1
    dfs(n+1, nsum  + height[n])
    v[n] = 0
    dfs(n+1, nsum)
        
    


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int,input().split()))
    # 최솟값 설정을 위한 큰 수
    min_value = 9999999
    # 조합으로 뽑을 때 방문처리를 위함
    v = [0] * N
    dfs(0,0)
    print(f'#{tc} {min_value- B}')
    