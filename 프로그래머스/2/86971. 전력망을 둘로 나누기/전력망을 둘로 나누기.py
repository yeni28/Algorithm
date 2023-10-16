from collections import deque

def solution(n, wires):
    res = 0
    # 0이 아닌 리스트로 받는구나.
    graph = [[] for _ in range(n+1)]
    
    #[a,b]형태의 값을 받을 때 이렇게 받을 수 있다.
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visited = [0] * (n+1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
    
    res = n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(bfs(a) - bfs(b)), res)
        
        
        #dfs 끝났으면 다시 추가
        graph[a].append(b)
        graph[b].append(a)
          
    return res

