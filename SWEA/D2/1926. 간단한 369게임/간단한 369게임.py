N = int(input())

for i in range(1, N+1):
    cnt = 0
    for n in str(i):
        if n == '3' or n == '6' or n =='9':
            cnt += 1
    if cnt == 0:
        print(i, end=" ")
    else:
        print('-' * cnt, end=" ")
