def solution(array, commands):
    answer = []
    for i in commands:
        ans = []
        for idx in range(i[0]-1,i[1]):
            ans.append(array[idx])
        #정렬해주기
        ans.sort()
        answer.append(ans[i[2]-1])
    return answer