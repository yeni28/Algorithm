N, K = map(int, input().split())
array = list(map(int,input().split()))
sort_arr = sorted(array)
print(sort_arr[K-1])