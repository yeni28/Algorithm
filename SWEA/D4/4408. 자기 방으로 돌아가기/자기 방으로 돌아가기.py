T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [0] * 401
    #과거 방번호의 기록(1->3, 4->6은 안돼도 2->4, 5->7은 되는문제 해결을 위해)
    pre_backroom = 0
    for i in range(N):
        now_room, back_room = map(int, input().split())
        if now_room < back_room:
            if now_room % 2 ==0 and now_room - 1 == pre_backroom:
                rooms[now_room] += 2
                pre_backroom = back_room
            else:
                # 방의 범위를 다 더해서, 지나간 길이 겹치면 가장 큰수가 기다림의 수!
                for r in range(now_room, back_room + 1):
                    rooms[r] += 1
                pre_backroom = back_room
        elif now_room > back_room:
            if now_room % 2 ==0 and now_room - 1 == pre_backroom:
                rooms[now_room] += 2
                pre_backroom = back_room
            else:
                for r in range(back_room, now_room+ 1):
                    rooms[r] += 1
                pre_backroom = back_room
        #방이 같다면 안더해줌(이동안함)
        elif now_room == back_room:
            if now_room % 2 ==0 and now_room - 1 == pre_backroom:
                rooms[now_room] += 2
                pre_backroom = back_room
            else:
                rooms[r] += 0
                pre_backroom = back_room

    print(f'#{tc} {max(rooms)}')
