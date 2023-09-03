a = int(input())
b= input()
b_lst = list(b)

for i in range(3):
    if i == 0:
        one = a*int(b_lst[i])
    if i == 1:
        two = a*int(b_lst[i])
    if i == 2:
        three = a*int(b_lst[i])
print(three)
print(two)
print(one)
print(one * 100 + two*10 + three)