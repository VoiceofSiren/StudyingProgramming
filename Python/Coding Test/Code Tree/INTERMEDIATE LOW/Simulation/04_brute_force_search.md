# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/conveyor-belt-triangle?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 2차원 배열의 각 행의 마지막 원소를 임시 변수에 할당한 후 각 행에서 오른쪽으로 한 칸씩 shift 시킨 후,
- 1행의 임시 변수의 값을 2행의 첫 번째 요소에, 2행의 임시 변수의 값을 1행의 첫 번째 요소에 할당하는 로직을 구현하고자 한다.
#### [코드 1-1]
```python
n, t = list(map(int, input().split()))
c_belt = [list(map(int, input().split())) for _ in range(2)]
```
