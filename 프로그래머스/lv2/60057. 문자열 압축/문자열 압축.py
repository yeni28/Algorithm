def solution(s):
    N = len(s)
    result = []
    if N ==1:
        return 1
    for i in range(1, N+1):
        b = ''
        cnt = 1
        tmp = s[:i]
        
        #i부터 끝까지 i 단위로 나누어 탐색
        for j in range(i, N+i, i):
            if tmp == s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b+ str(cnt) + tmp
                else:
                    b = b+tmp
                tmp = s[j:j+i]
                cnt = 1
        result.append(len(b))
    return min(result)