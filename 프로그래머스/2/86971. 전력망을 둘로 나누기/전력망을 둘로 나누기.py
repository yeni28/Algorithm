from collections import deque

def solution(n, wires):
    graph  = [[] for _ in range(n+1)]
    
    # 각 노드의 연결을 표현하는 배열
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 전력망 노드 연결 확인할 bfs 만들어주기
    def bfs(start):
        visited = [0] * (n+1)
        visited[start] = 1
        q = deque([start])
        # 노드 연결 수 체크할 cnt
        cnt =1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1
        return cnt
    
    res = n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(bfs(a)- bfs(b)), res)
        
        graph[a].append(b)
        graph[b].append(a)
        
        
    

    return res