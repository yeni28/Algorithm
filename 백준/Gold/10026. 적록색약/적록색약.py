import sys
sys.setrecursionlimit(10 ** 6)  # 파이썬의 재귀 깊이 지정 (Python3)
input = sys.stdin.readline
N = int(input())

area = []
visited = [[0] * (N) for _ in range(N)]
sum = 0
sum2 = 0

# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N):
    area.append(list(input()))

def dfs(i, j, color):
    visited[i][j] = 1

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if area[ni][nj] == color:
                dfs(ni, nj, color)


for color in ['R', 'G', 'B']:
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] == color:
                dfs(i, j, color)
                sum += 1

for i in range(N):
    for j in range(N):
        if area[i][j] == 'G':
            area[i][j] = 'R'

visited = [[0] * (N) for _ in range(N)]

for color in ['R', 'B']:
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] == color:
                dfs(i, j, color)
                sum2 += 1

print(sum, sum2)