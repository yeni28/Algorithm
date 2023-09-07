import math

def solution(progresses, speeds):
    answer = []
    works = []
    N = len(speeds)
    for i in range(N):
        works.append(100 - int(progresses[i]))
    remains = []
    for j in range(N):
        remains.append(math.ceil(int(works[j]) / int(speeds[j])))
    v = [0] * N

    for r in range(N):
        cnt = 0
        for n in range(0,N):
            # 다음 값이 나보다 작으면
            if r + n < N:
                if int(remains[r]) >= int(remains[r + n]) and v[r+n] == 0 :
                    cnt += 1
                    v[r+n] = 1
                else:
                    break
        if cnt != 0:
            answer.append(cnt)
    return answer