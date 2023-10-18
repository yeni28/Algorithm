def solution(word):
    
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt,w):
        if cnt == 5:
            return
        else:
            for i in range(5):
                word_list.append(w + words[i])
                dfs(cnt+1, w+words[i])
    dfs(0,'')
        
    
    return word_list.index(word) + 1