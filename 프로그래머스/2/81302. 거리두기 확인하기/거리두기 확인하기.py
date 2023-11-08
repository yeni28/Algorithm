from collections import deque
    
def bfs(cls):
    
    # P의 위치에서만 검사
    start = []
    for i in range(5):
        for j in range(5):
            if cls[i][j] == 'P':
                start.append([i, j])
    
    for x,y in start:
        q = deque([])
        # 큐에 초기값 추가하기
        q.append([x,y])
        visited = [[0]*5 for i in range(5)]  
        # 맨해튼 거리 검사
        distance = [[0]*5 for i in range(5)]  
        visited[x][y] = 1
        
        while q:
            y, x = q.popleft()
        
            dx = [-1, 1, 0, 0]  
            dy = [0, 0, -1, 1]  

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if cls[ny][nx] == 'O':
                        q.append([ny, nx])
                        #방문처리
                        visited[ny][nx] = 1
                        # 거리처리
                        distance[ny][nx] = distance[y][x] + 1
                    # 거리가 맨해튼 이하면
                    if cls[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for cls in places:
        answer.append(bfs(cls))
    
    return answer
            
