
def dfs(n, lst):
    if n == M: #M개를 다 골랐나요?
        ans.append(lst) #그렇다면 리스트에 추가해주세용
        return
    for j in range(1,N+1): #1에서 N까지 자연수 중에서
        # 여기서 하나를 고르고 또 M까지 숫자를 고르는 리스트를 추가해주는 것
        dfs(n+1, lst+[j]) #리스트에 j를 담아서 다음 숫자와 고르는 함수를 맹글어줘요


N, M = map(int, input().split())
ans = [] # 정답 리스트 입니다
dfs(0, [])
for lst in ans:
    print(*lst)