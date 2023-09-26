ans = 0

def solution(numbers, target):
    M = len(numbers)
    nsum = 0
    def dfs(n, nsum):
        global ans
        #리스트의 값을 모두 사용했나요?
        if n == M:
            #타겟값과 sum값이 같다면
            if nsum == target:
                ans += 1
                return
        else:
            dfs(n + 1, nsum +numbers[n])
            dfs(n + 1, nsum- numbers[n])
    dfs(0,0)

    answer = ans
    return answer