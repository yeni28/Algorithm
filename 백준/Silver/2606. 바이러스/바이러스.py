computers = int(input())
link_num = int(input())

#서로 연결되어있는 것 확인하는 배열
graph = [[0]*(computers+1) for _ in range(computers+1)]
for i in range(link_num):
    # 연결 되어있고 안되어 있고, 이것을 배열에 넣을 것입니다!
    a,b = map(int,input().split())
    # 연결 되어있는 상태를 1로 표시해줍니다.
    graph[a][b] = graph[b][a] = 1

#방문체크
v = [0] * (computers+1)
s = []
link = set()
ans = 0
for i in range(1,computers+1):
    if v[i]:
        continue
    else:
        v[i] = 1
        s=[i]
        while s:
            node = s.pop()
            for c in range(1,computers+1):
                if graph[node][c] and not v[c]:
                    if node == 1:
                        link.add(c)
                    if c in link or node in link:
                        link.add(node)
                        link.add(c)
                        ans += 1
                    # 1번과 연결되어있는 것을 확인하는 조건을 추가함.
                    v[c] =1
                    s.append(c)
print(ans)

