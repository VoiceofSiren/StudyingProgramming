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
- 인접 리스트를 adjacent_list, Vertex의 총 개수를 n이라고 할 때,
  인접 리스트의 초기 상태를 adjacent_list = [ [ 0 for _in range(n) ] for _ in range(n) ] 로 정의할 수 있다.
```
```plaintext
- v1번째 vertex를 vtx_1, v2번째 vertex를 vtx_2라고 할 때
  vtx_1과 vtx_2가 서로 연결되어 있으면 adjacent_list[v1][v2] = 1,
  vtx_1과 vtx_2가 서로 연결되어 있지 않으면 adjacent_list[v1][v2] = 0 과 같은 방식으로 값을 부여할 수 있고,
  이는 매우 가시성이 좋은 편이다.
```
```plaintext
- 다만, 시간 복잡도가 O(N^2)이기 때문에 Vertex의 개수가 점점 늘어날수록 성능은 기하급수적으로 악화된다. 
```
#### 2) 인접 리스트
```plaintext

```

### < 구현 과정 - 1 >
- 인접 행렬과 
#### [코드 1-1]
```python
