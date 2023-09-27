from collections import deque

N, M, V = map(int, input().split())
graph = [[0] *(N+1) for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)



def dfs(n):
    visited1[n] = 1
    print(n, end=' ')
    for i in range(1,N+1):
        if graph[n][i] ==1 and visited1[i]== 0:
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited2[n] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in range(1,N+1):
            if visited2[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited2[i] = 1


dfs(V)
print()
bfs(V)

