whole_score = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        whole_score += 40
    else:
        whole_score += score
print(whole_score//5)