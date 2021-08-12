
# TODO Learn 4881 배열최소합.
def per(k, midV):
    # 최솟값 가져오기.
    global minV
    # 가지치기.
    if minV < midV:
        return # return 받을 거 없을 때는 값 안적어줘도 됨.함수 끝내는 용도.
    # 재귀로 k가 배열 길이만큼 되었을때 최솟값 비교해서 구하기.
    # 백트래킹을 이용..
    if k == N:
        if minV > midV:
            minV = midV
    for i in range(N):
        # 세로열 당 1개씩이므로 방문한 곳 체크.
        if not visited[i]:
            #sel[k] = i
            visited[i] = True
            per(k+1, midV + BRD[k][i]) # 다음 열로 넘어감, 자리 중요.
            visited[i] = False
            
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    BRD = [list(map(int, input().split())) for _ in range(N)]
    minV = 1e1000000 # 최솟값 초기설정..
    visited = [False] * N # 방문한 곳 기록..
    #sel = [-1] * N # : 순열 데이터
    per(0, 0)
    print('#{} {}'.format(tc, minV))
