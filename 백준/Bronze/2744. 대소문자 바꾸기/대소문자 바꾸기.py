word = input()
n = ""
for w in word:
    if w.islower():
        n += w.upper()
    else:
        n += w.lower()
print(n)