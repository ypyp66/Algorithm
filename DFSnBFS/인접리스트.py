# 인접리스트는 연결된 정보만을 저장함

graph = [[] for _ in range(3)]

graph[0].append((1,7)) #0번 노드 -> 1번 노드의 거리는 7
graph[0].append((2,5)) #0번 노드 -> 2번 노드의 거리는 5

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)