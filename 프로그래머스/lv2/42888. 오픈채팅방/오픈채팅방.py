from collections import defaultdict        

def solution(record):
    answer = []
    N = len(record)
    actions = [[] * len(record)]
    user = defaultdict()
    # 띄어쓰기 별로 나눠줌
    for action in record:
        actions.append(action.split())
    
    #이름 체크해줌
    for i in actions:
        if i :
            for j in range(len(i)):
                if 0 < j and j + 1 < len(i):
                    user[i[j]] = i[j+1]
                    
    # print(user)
    for order in actions:
        sentence = ''
        username = ''
        action = ''
        if order:
            for j in range(len(i)):
                if 0 < j < 2:
                    username = user[order[j]] + '님이'
                if j == 0:
                    if order[j] == 'Enter':
                        action = '들어왔습니다.'
                    elif order[j] == 'Leave':
                        action = '나갔습니다.'
                    else:
                        continue
        if action:
            sentecne = sentence + username + ' ' + action
            answer.append(sentecne)                    
    return answer