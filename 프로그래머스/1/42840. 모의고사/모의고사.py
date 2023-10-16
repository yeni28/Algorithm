def solution(answers):
    # 찍는 방식은 패턴이 반복된다.
    # 최대 10000문제 중 일치하는 것이 가장 많은 수포자!
    # 똑같을 경우 오름차순으로 정렬!
    
    sol1 = [1,2,3,4,5] * 2000
    sol2 = [2,1,2,3,2,4,2,5] * 1250
    sol3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    ans1 = 0
    ans2 = 0
    ans3 = 0
    
    for i in range(len(answers)):
        if answers[i] == sol1[i]:
            ans1 +=1
        if answers[i] == sol2[i]:
            ans2 +=1        
        if answers[i] == sol3[i]:
            ans3 +=1
    
    ans_list = [ans1,ans2,ans3]
    
    maxv = max(ans_list)
    answer = []
    for k in range(3):
        if ans_list[k] == maxv:
            answer.append(k+1)
            
        
        
    answer.sort()
    return answer