def dfs(n, lst):
    #종료 조건(n에 관련된 형태) 처리 + 정답처리
    if n == M : # M개의 수열을 완성했을 때
        ans.append(lst)
        return
    
    #하부(단계) 함수 호출
    for j in range(1, N+1):
        if v[j] == 0: # 선택하지 않은 숫자인 경우
            v[j] = 1
            dfs(n+1, lst+[j])
            # 다녀와서는 0으로 초기화 해줘야한다.
            v[j] = 0

N, M = map(int, input().split())
ans = [] # 정답 리스트를 저장할 리스트
v = [0] *(N+1) # 중복 확인을 위한 visited 배열

dfs(0,[])
for lst in ans:
    print(*lst)
