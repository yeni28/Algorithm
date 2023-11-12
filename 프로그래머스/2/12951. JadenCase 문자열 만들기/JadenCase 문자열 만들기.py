def solution(s):
    answer = ''

    for i in range(len(s)):
        if i == 0:
            if type(s[i]) == 'int':
                answer += str(s[i])
            else:
                answer += s[i].upper()
        else:
            if s[i-1] == " ":
                answer += s[i].upper()
            else:
                answer += s[i].lower()
    return answer