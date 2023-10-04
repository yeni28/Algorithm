max_num = 0

def solution(number, k):
    num = ''
    N = len(number)
    a = N-k
    number = list(number)
    def dfs(n,num,number):
        global max_num
        # 수의 조합을 다 썼나요?
        if n == a:
            if int(num) >= max_num:
                max_num = int(num)
            return

        else:
            for i in range(N):
                #중복 제거
                number.pop(number[i])
                dfs(n+1,num + number[i],number)
                
    dfs(0,num,number)
        
    answer = max_num
    return answer