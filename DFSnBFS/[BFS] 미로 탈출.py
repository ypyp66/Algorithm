from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

'''
시작위치 = (1,1)
(0,0) ~ (n,m) 까지의 최단 거리

풀이 방법
- 현재 위치에서 상하좌우를 검색하고 노드값이 1인 경우 방문 후 값을 +1
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # (x,y) 꼴로 좌표 저장

    while queue: #queue가 빌때까지 반복
        x,y = queue.popleft() # (x,y)꼴 이므로

        for i in range(4): # 현재위치에서 4방향으로 확인 (상하좌우)
            #상 : (x-1, y), 하: (x+1, y), 좌: (x, y-1), 우: (x, y+1) 이므로 dx,dy를 저렇게 설정한다
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >=n or ny >=m: #범위를 벗어난 경우
                continue #dfs와는 다르게 pass해준다
            
            if graph[nx][ny] == 0: # 못가는 자리면 pass
                continue

            if graph[nx][ny] == 1: # 갈수있는 곳이면
                graph[nx][ny] = graph[x][y] + 1 # 현재값에 +1 해줌
                queue.append((nx,ny))
    return graph[n-1][m-1] # 가장 끝 값 반환

print(bfs(0,0))

"""
(0,0)에서 시작 및 큐에 삽임
큐에서 꺼내기 -> 상하좌우 검증 후 가능한 좌표값 = 현재값+1 후 좌표를 큐에 삽입 -> 반복
"""