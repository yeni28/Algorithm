from collections import deque

def solution(n, wires):
    
    #연결을 표현할 그래프를 만든다.
    graph = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    # 연결 노드 찾기
    def bfs(start):
        visited = [0] * (n+1)
        visited[start] = 1
        q = deque([start])
        cnt = 1 
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    cnt +=1
        return cnt

    res = n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(bfs(b)-bfs(a)),res)
        
        graph[a].append(b)
        graph[b].append(a)
    
    
    return res