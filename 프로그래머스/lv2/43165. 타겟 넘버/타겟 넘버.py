ans = 0
def solution(numbers, target):
    result = 0
    def dfs(n, result):
        global ans
        if n == len(numbers):
            if result == target:
                ans += 1
            return
        dfs(n+1, result + numbers[n])
        dfs(n+1, result - numbers[n])
    
    dfs(0,0)
    answer = ans
    return answer