
graph = [
  [],                 # 1번 노드와 연결된 노드들
  [2, 3, 8],          # 2번 노드와 연결된 노드들
  [1, 7],             # 3번 노드와 연결된 노드들
  [1, 4, 5],          # 4번 노드와 연결된 노드들
  [3, 5],             # 5번 노드와 연결된 노드들
  [3, 4],             # 6번 노드와 연결된 노드들
  [7],                # 7번 노드와 연결된 노드들
  [2, 6, 8],          # 8번 노드와 연결된 노드들
  [1, 7]              # 9번 노드와 연결된 노드들
]

def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
             DFS(graph,i,visited)

visited = [False] * 9

DFS(graph,1,visited)