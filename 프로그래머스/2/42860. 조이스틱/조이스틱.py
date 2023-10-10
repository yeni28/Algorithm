def solution(name):
    answer = 0
    N = len(name)
    min_moves = N - 1 
    first = 'A' * N
    tmp = 0
    for i in range(0,N):
        # 상하 이동 계산
        up = ord(name[i]) - ord('A')
        down = ord('Z') - ord(name[i]) + 1
        move1 = min(up, down)
        
        next_pos = i + 1
        while next_pos < N and name[next_pos] == 'A':
            next_pos += 1
        move2 = min(i, N - next_pos)  # 왼쪽으로 이동한 거리와 오른쪽으로 이동한 거리 중 최소값 선택
        min_moves = min(min_moves, i + N - next_pos + move2)
        
        answer += move1

    return answer + min_moves

    
