from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    ans = []
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance  = [-1] * (n+1)
    distance[1] = 0
    q  = deque([1])
    
    while q:
        s = q.popleft()
        for i in graph[s]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[s] + 1
                
    
    #1번 노드에서 가장 멀리 떨어진 노드 (1번 노드까지의 거리)
    for d in distance :
        if d == max(distance):
            answer +=1
            
        
    
    return answer