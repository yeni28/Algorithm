def solution(n, computers):
    answer = 0
    #방문 배열을 만들어 준다.
    visited = [0] * n
    
    # for문을 돌면서 node 값을 탐색한다.
    for r in range(n):
        # 만약 방문했었다면,
        if visited[r]:
            #넘어감
            continue
        # 노선 값에 +1 해준다.
        answer += 1
        #방문처리를 해준다.
        visited[r] = 1
        # stack 에 r을 넣어준다.
        s = [r]
        # s가 있는동안
        while s:
            # node는 s리스트에서 빼고
            node = s.pop()
            # n을 돌면서 확인을 해주는거야.
            for c in range(n):
                # 리스트의 node c가 있고(1이고), 방문 한 적이 없다면
                if computers[node][c] and not visited[c]:
                    #방문처리를 해주고
                    visited[c] = 1
                    # 스택에 넣어준다.
                    s.append(c)

    return answer