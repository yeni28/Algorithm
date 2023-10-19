cnt = 0 
def solution(numbers, target):
    
    #numbers 리스트
    
    def dfs(n, num):
        global cnt
        if n == len(numbers):
            if num == target:
                cnt += 1 
                return
        else:
            dfs(n+1, num + numbers[n])
            dfs(n+1, num - numbers[n])
    
    dfs(0,0)

        
    return cnt