N = int(input())
n_list = [0] * N
for i in range(N):
    n_list[i] = int(input())

n_list.sort()
for n in n_list:
    print(n)