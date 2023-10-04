
N = int(input())
map  = [list(map(int, input())) for _ in range(N)]


#방문배열
visited = [[0]*N for _ in range(N)]

#상하좌우
di = [-1,1,0,0]
dj = [0,0,-1,1]
danji = 0
danji_list = []
def dfs(i,j):
    global danji
    #방문처리
    visited[i][j] = 1
    danji += 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == 0 and map[ni][nj] !=0:
                dfs(ni,nj)

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            danji_list.append(danji)
            danji = 0
danji_list.sort()

print(len(danji_list))
for k in danji_list:
    print(k)