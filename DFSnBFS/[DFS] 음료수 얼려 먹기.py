n,m = map(int, input().split())


graph = []
for i in range(n): #0~(n-1)
    graph.append(list(map(int, input()))) #이렇게해도 리스트로 저장됨
"""
문제 풀이 방법
1. 특정한 지점의 주변(상,하,좌,우)를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 
   아직 방문하지 않은 지점이 있다면 해당 지점을 방문

2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 다시 진행 (재귀) 
"""

def dfs(x,y): #그래프는 (x,y)형태 이므로
    #먼저 범위가 벗어나면 끝나게 설정함
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0: #현재 좌표의 값이 0이면 (채울수 있다면)
        graph[x][y] = 1 #방문 했으므로 1로 바꿔준다
        #상하좌우 모두 재귀로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False #좌표가 1이면 false를 return

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)
