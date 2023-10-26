from collections import defaultdict

def solution(s):
    s_dict = defaultdict(list)
    s = s.replace("{","").replace("}","").split(",")
    
    
    for c in s :
        c = int(c)
        
        if c in s_dict:
            s_dict[c] += 1
        else:
            s_dict[c] = 1
    answer = sorted(s_dict, key=lambda x: s_dict[x], reverse = 1)
    return answer
