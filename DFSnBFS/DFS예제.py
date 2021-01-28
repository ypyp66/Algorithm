#인접리스트
graph = [
    # 총 9줄
    # 각 줄은 노드의 번호
    # 내용은 노드에 인접한 노드 목록
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def dfs(v):
    global visited, graph
    visited[v] = True #현재 노드를 방문처리 (일단 시작인 첫번째 노드 방문처리)
    print(v, end=' ')

    for i in graph[v]: #graph[1]의 요소를 하나씩 검사
        if not visited[i]:
            dfs(i)



'''
처음에 1번 노드에서 시작 -> 1번 방문처리                                                          => 1
graph[1][0] = 2 이므로 2번 노드 방문 -> 2번 방문처리 및 dfs(2) 호출                               => 2
ㄴgraph[2][0] = 1, 이미 방문 했으므로 graph[2][1] = 7번 노드 방문 -> 7번 방문처리 및 dfs(7) 호출   => 7
  ㄴgraph[7][0] = 2, 이미 방문 했으므로 graph[7][1] = 6번 노드 방문 -> 6번 방문처리 및 dfs(6) 호출 => 6
    ㄴgraph[6][0] = 7, 이미 방문 했으므로 2번 노드로 되돌아감, graph[7][2]차례
  ㄴgraph[7][2] = 8번 노드 방문처리 및 dfs(8) 호출                                               => 8
    ㄴgraph[8][0] = 1, 이미 방문 했으므로 graph[8][1] = 7, 이미 방문 했으므로 graph[2][1]차례
ㄴgraph[2][1] = 7, 이미 방문 했으므로 graph[1][1] 차례

graph[1][1] = 3 이므로 3번 노드 방문 -> 3번 방문처리 및 dfs(3) 호출                               => 3
ㄴgraph[3][0] = 1, 이미 방문 했으므로 graph[3][1] = 4번 노드 방문 -> 4번 방문처리 및 dfs(4) 호출   => 4
  ㄴgraph[4][0] = 3, 이미 방문 했으므로 graph[4][1] = 5번 노드 방문 -> 5번 방문처리 및 dfs(5) 호출 => 5
    ㄴgraph[5][0] = 3, 이미 방문 했으므로 graph[5][1] = 4, 이미 방문 했으므로 graph[3][1] 차례
ㄴgraph[3][1] = 4, 이미 방문 했으므로 graph[3][2] = 5, 이미 방문 했으므로 graph[1][2] 차례

graph[1][2] = 8, 이미 방문 했으므로 더이상 갈 곳이 없으므로 끝남


### 해당 노드에 인접한 노드중 방문하지 않은 노드가 있으면 바로 이동
### 스택 및 재귀함수를 이용한다
'''

#각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(1) #graph[0]는 없으므로 1부터 시작