# DFS (Depth First Search)
###### Question: https://www.codetree.ai/missions/2/problems/graph-traversal?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - DFS (깊이 우선 탐색) 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### 구현에 앞서
- 그래프 상에서 DFS 기법을 사용하기 위해 사용되는 자료 구조는 일반적으로 인접 행렬과 인접 리스트이다.
#### 1) 인접 행렬
```plaintext
- 인접 행렬을 adjacent_matrix, Vertex의 총 개수를 n이라고 할 때,
  인접 행렬의 초기 상태를 adjacent_matrix = [ [ 0 for _in range(n) ] for _ in range(n) ] 로 정의할 수 있다.
```
```plaintext
- v1번째 vertex를 vtx_1, v2번째 vertex를 vtx_2라고 할 때
  vtx_1과 vtx_2가 서로 연결되어 있으면 adjacent_matrix[v1][v2] = 1,
  vtx_1과 vtx_2가 서로 연결되어 있지 않으면 adjacent_matrix[v1][v2] = 0 과 같은 방식으로 값을 부여할 수 있고,
  이는 매우 가시성이 좋은 편이다.
```
```plaintext
- 다만, 시간 복잡도가 O(N^2)이기 때문에 Vertex의 개수가 점점 늘어날수록 성능은 기하급수적으로 악화된다. 
```
#### 2) 인접 리스트
```plaintext
- 비어있는 2차원 리스트 adjacent_list를 만들고 임의의 Vertex에 대하여 직접적으로 연결되어 있는 모든 Vertex들의 값을 append하는 방식으로 구현한다.
```
```plaintext
- 상황에 따라 정점을 방문했는지 여부를 체크하는 1차원 리스트를 추가로 사용해야 하는 경우도 있다.
```
```plaintext
- 모든 Vertex의 개수를 V, 모든 Edge의 개수를 E라고 할 때 시간 복잡도가 O(V + E)이기 때문에 인접 행렬을 사용하는 경우보다 성능 측면에서 훨씬 우수하다.
```
#### --> 위와 같은 요인에 따라 필자는 인접 리스트를 사용한 DFS 기법을 통해 구현할 것이다.
<br/>

### < 구현 과정 - 1 >
- Recursive call 방법을 사용하여 문제를 해결해볼 것이다.
#### [코드 1-1]
```python
n, m = tuple(map(int, input().split()))

graph = [
    [] for _ in range (n + 1)
]

visited = [
    False for _ in range(n + 1)
]


for i in range(m):
    start, end = tuple(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)
```
#### [코드 1-2]
```python
vertex_count = 0

def dfs(current_vertex):
    global vertex_count

    for adjacent_vertex in graph[current_vertex]:

        if not visited[adjacent_vertex]:
            visited[adjacent_vertex] = True
            vertex_count += 1
            dfs(adjacent_vertex)
```
#### [코드 1-3]
```python
visited[1] = True
dfs(1)
print(vertex_count)
```
#### [결과 1]
```plaintext
2
```
