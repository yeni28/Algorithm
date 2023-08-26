def password(lst):
    global stop
    K = len(lst)
    for i in range(K):
        if i + 1 <= K-1:
            if lst[i] == lst[i+1]:
                lst.pop(i)
                lst.pop(i)
                password(lst)
            #재귀 종료조건
            if stop == True:
                return lst
            else:
                if i != K-1:
                    continue
                else:
                    #재귀 종료조건
                    stop = True
                    return lst

        else:
            #재귀 종료조건
            stop = True
            return lst

for tc in range(1, 11):
    stop = False
    #앞에 0이 들어오므로 int로 받으면 안됨
    n, num = input().split()
    N = int(n)
    numlst = [0] * N
    for i in range(N):
        numlst[i] = int(num[i])
    pw = password(numlst)
    ans =''
    for p in pw:
        ans += str(p)
    print(f'#{tc} {ans}')