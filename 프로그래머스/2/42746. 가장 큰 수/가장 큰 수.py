def solution(numbers):
    s = list(map(str,numbers))
    a = sorted(s, key=lambda x : x*3, reverse=True)
    
    return str(int("".join(a)))