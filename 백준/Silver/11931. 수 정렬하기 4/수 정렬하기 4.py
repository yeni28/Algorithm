import sys

N = int(sys.stdin.readline())
numlist = []
for i in range(N):
    numlist.append(int(sys.stdin.readline()))

numlist.sort()
numlist.reverse()

for i in numlist:
    print(i)
