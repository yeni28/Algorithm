
n_list = []
for _ in range(28):
    n = int(input()) 
    n_list.append(n)

for k in range(1,31):
    if k not in n_list:
        print(k)
    