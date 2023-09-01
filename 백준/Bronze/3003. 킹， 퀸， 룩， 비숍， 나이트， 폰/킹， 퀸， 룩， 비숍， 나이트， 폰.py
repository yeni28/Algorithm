lst = [1,1,2,2,2,8]
c_lst = list(map(int, input().split()))
ans = []
for i in range(6):
    ans.append(lst[i]- c_lst[i])

print(*ans)