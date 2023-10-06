answer = -1
def solution(k, dungeons):
    #행은 8이하 열은 2 고정
    # 최필피 >= 소모
    # 서로다른 던전의 최필피, 소모가 같을 수 있다.
    #k는 현재피로도
    visited = [0] * (len(dungeons)+ 1)
    dfs(k,0, dungeons, visited)
    return answer



def dfs(tired, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)
    for d in range(len(dungeons)):
        # 최필피보다 크면
        if tired >= dungeons[d][0] and visited[d] == 0:
            #방문처리
            visited[d] = 1
            # 소모피로를 깎고 이동
            # 경로 처리
            dfs(tired - dungeons[d][1], cnt +1, dungeons ,visited)
            visited[d] = 0

        