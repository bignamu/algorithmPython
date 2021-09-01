import math
from collections import deque

Board = []
Allcard = {}
Allremoved = 1 # 비트의 0번째가 켜져있다는 뜻 [0,...,0,0,1]
MinCnt = math.inf # 최소 조작 횟수
D = ((-1,0),(1,0),(0,-1),(0,1)) # 상하좌우로 이동


def bfs(removed,src,dst): #비트0, 출발지 ,목적지
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = deque()
    q.append(src)
    while q:
        
        curr = q.popleft()
        # print(curr)
        if curr[0] == dst[0] and curr[1] == dst[1]: # [0]이 row를 뜻한다 [1]이 col 즉 , 행과열이 같다면
            return  curr[2] #조작횟수는 [2]에 있음
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 3 or nc < 0 or nc > 3:
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc,curr[2]+1))

            # Ctrl + 화살표 처리
            for j in range(2): # 끝에서 끝으로 움직일때 최대 움직이는 거리
                if (removed & 1 << Board[nr][nc]) == 0: # 카드가 존재하는 경우 멈추는 것
                    break
                if nr +D[i][0] < 0 or nr + D[i][0] > 3 or nc + D[i][1] < 0 or nc + D[i][1] > 3:
                    break
                nr += D[i][0]
                nc += D[i][1]
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc,curr[2]+1))
    return math.inf
def permutate(cnt,removed,src): # removed는 지금까지 삭제된 카드를 비트 형태로 나타낸거임
    global MinCnt 
    
    if cnt >= MinCnt:
        return

    if removed == Allremoved: #카드가 제거될때마다 removed의 비트를 왼쪽으로 밀어줌
        MinCnt = min(MinCnt,cnt)
        return
    
    for num, card in Allcard.items(): # card는 리스트로 나옴
        if removed & 1 << num: # 이 숫자가 이미 삭제된 것이면 스킵한다
            continue
        one = bfs(removed,src,card[0]) + bfs(removed,card[0],card[1]) + 2 # 순차 src 출발지,card[0]카드위치 => card[0]에서 card[1]로 가는 횟수 + 엔터 2번 
        two = bfs(removed,src,card[1]) + bfs(removed,card[1],card[0]) + 2 # 역순
        
        permutate(cnt+one,removed | 1 << num,card[1])
        permutate(cnt+two,removed | 1 << num,card[0])

def solution(board, r, c):
    answer = 0
    global Board, Allremoved,Allcard
    Board = board
    for i in range(4):
        for j in range(4):
            num = Board[i][j]
            if num:
                Allremoved |= 1 << num # [1] => num만큼 왼쪽으로 밀어버리는거임 [1,0] [1,0,0] 즉 , 카드 갯수만큼 밀어버리는거임 일종의 count
                if num in Allcard:
                    Allcard[num].append((i,j,0))
                else:
                    Allcard[num] = [(i,j,0)]
    # print(Allcard)
    permutate(0,1,(r,c,0))
    answer = MinCnt
    return answer





board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
# 14

solution(board,r,c)