
def solution(s):
    arr = list(map(int, s.split(' ')))         
    arr.sort()                                  # int로 이루어진 배열을 sort
    return str(arr[0]) + " " + str(arr[-1])  