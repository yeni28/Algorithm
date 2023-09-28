def solution(n, lost, reserve):
    ans = len(lost)
    v = [0] * 31
    lost = sorted(lost)
    reserve = sorted(reserve)
    babo = []
    for i in range(len(lost)):
        if lost[i] in reserve:
            ans -= 1
            reserve.remove(lost[i])
            babo.append(lost[i])

    for l in babo:
        lost.remove(l)

    # 로스트에서 하나 뺌
    while lost:
        student = lost.pop()
        #도둑 맞은 학생 중에 여벌을 가지고 온 애들이 있나?

        for r in range(len(reserve)-1,-1,-1):
            if abs(student - reserve[r]) == 1 and not v[reserve[r]]:
                v[reserve[r]] = 1
                ans -= 1
                break
    answer = n - ans
    return answer