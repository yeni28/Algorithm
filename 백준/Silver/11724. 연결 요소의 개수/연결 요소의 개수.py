import sys

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

v = [0] * (N+1)
s = []
ans = 0
for i in range(1,N+1):
    if v[i]:
        continue
    else:
        # 방문체크
        v[i] = 1
        # 스택에 넣기
        s = [i]
        # 간선은 처리해주기
        ans +=  1
        while s:
            node = s.pop()
            for c in range(1, N+1):
                # 연결되어있고, 방문한 적이 없으면
                if graph[node][c] and v[c] ==0:
                    v[c] = 1
                    s.append(c)
print(ans)