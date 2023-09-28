ans = 0
def solution(numbers, target):
    # nubers는 리스트, 타겟은 int값
    # 뽑는 숫자의 수가 정해져있으므로 백트래킹을 사용해보자.
    # 뽑아서 nsum이 target이 되면 그 값을 global 변수에 담아 더해준다.
    def dfs(n, nsum):
        global ans
        # 숫자를 다 뽑았으면
        if n == len(numbers):
            # 그 합의 값이 target과 같으면
            if nsum == target:
                ans += 1
                return
        else:
            dfs(n+1, nsum + numbers[n])
            dfs(n+1, nsum - numbers[n])
        
    dfs(0,0)
    answer = ans
    
    return answer