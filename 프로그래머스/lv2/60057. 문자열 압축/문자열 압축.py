def solution(s):
    N = len(s)
    result = []
    #문자열을 i부터 N단위 까지 자를 것입니다.
    for i in range(1,N+1):
        # 압축된 것을 반환할 문자열
        sentence = ''
        # 중복 개수를 체크할 숫자
        cnt = 1
        #미리 자른 문자열
        tmp = s[:i]
        for j in range(i,N+i,i):
            # 만약 tmp랑 같으면(반복되는 문자열이면)
            if s[j:i+j] == tmp:
                #카운트 추가
                cnt += 1
            #반복 아니면
            else:
                #반복된 문자열이 있으면
                if cnt != 1:
                    sentence = sentence + str(cnt) + tmp
                else:
                    sentence = sentence + tmp
                #같지 않으니 tmp를 바꿔주고 cnt도 초기화 해준다.
                tmp = s[j:i+j]
                cnt = 1
        result.append(len(sentence))
    #이제 결과 값에 문장들이 모일것이다. 이중 가장 짧은 길이를 답으로 출력하면 된다.
        
    return min(result)

