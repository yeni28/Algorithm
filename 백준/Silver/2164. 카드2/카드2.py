from collections import deque

N = int(input())
card2 = deque()
for i in range(1, N+1):
    card2.append(i)

if len(card2) == 1:
    print(card2[0])
else:
    while True:
        card2.popleft()
        card2.append(card2[0])
        card2.popleft()
        if len(card2) == 1:
            print(card2[0])
            break

