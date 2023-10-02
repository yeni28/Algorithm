from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
v = [0] * (N + 1)
ans = [0] * (N+1)
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)

def dfs(graph, n, v):
    v[n] = 1
    s = deque([n])
    while s:
        node = s.pop()
        for c in graph[node]:
            if not v[c]:
                s.append(c)
                v[c] = 1
                ans[c] = node
dfs(graph,1,v)
for j in range(2, N + 1):
    print(ans[j])
