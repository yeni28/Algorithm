def solution(numbers):
    s = list(map(str,numbers))
    s = sorted(s , key=lambda x : x*3, reverse=True)
    
    return str(int(''.join(s)))