from collections import defaultdict

def solution(today, terms, privacies):
    d = defaultdict(list)
    answer = []
    t_term = list(map(int,today.split('.'))) 
    P = len(privacies)
    # 타입과 개월수 딕셔너리 저장
    for term in terms: 
        t_type, month = term.split()
        d[t_type] = int(month)*28

    for i in range(P):
        date, t_type = privacies[i].split()
        priv_term = list(map(int, date.split('.')))
        
        year = (t_term[0] - priv_term[0])*336 
        month = (t_term[1] - priv_term[1])*28 
        day = t_term[2] - priv_term[2]
        total = year+month+day
        # 남은 유효기간 날짜가 오늘과 과거 날짜의 차이보다 같거나 작으면 (유효기간 만료라면)
        # 인덱스 값에 1을 더해서 답에 추가해준다.
        if d[t_type] <= total:
            answer.append(i+1)
        
    return answer