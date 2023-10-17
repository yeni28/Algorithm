def solution(word):
    # 모음만 사용해 만들 수 있는 길이 최대 5이하 A=>UUUUU
    # 사전에서 몇 번째 단어인지
    
    answer = 0
    words ='AEIOU'
    # 단어를 만들어볼까요
    word_list = []
    # 각 최대 5개씩 쓸 수 있다.
    visited = [0] * (6)
    def dfs(cnt,w ):
        if cnt == 5:
            return
        for i in range(len(words)):
            word_list.append(w+words[i])
            dfs(cnt+1, w+words[i])
    
    dfs(0,'')
        
    
    return word_list.index(word) + 1