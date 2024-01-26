# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/conveyor-belt?&utm_source=clipboard&utm_medium=text
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
#### [코드 1-2]
```python
for i in range(t):
    temp1 = c_belt[0][n-1]
    temp2 = c_belt[1][0]

    for j in range(n-1, 1, -1):
        c_belt[0][j] = c_belt[0][j-1]
    c_belt[0][0] = temp1

    for j in range(n-2):
        c_belt[1][j] = c_belt[1][j+1]
    c_belt[1][n-1] = temp2
```
#### [코드 1-3]
```python
for i in range(2):
    for j in range(n):
        print(c_belt[i][j], end=' ')
    print()
```
#### [결과 1]
```plaintext
Traceback (most recent call last):
  File "/tmp/Main.py", line 1, in <module>
    n, t = list(map(int, input().split()))
    ^^^^
ValueError: not enough values to unpack (expected 2, got 1)
```
#### --> 
<br/>

### < 구현 과정 - 1 >
-
#### [코드 2-1]
```python
n, t = list(map(int, input().split()))
c_belt = [list(map(int, input().split())) for _ in range(2)]
```
#### [코드 2-2]
```python
time = 0
while time < t:
    temp1 = c_belt[0][n-1]
    temp2 = c_belt[1][n-1]
    for i in range(2):
        for j in range(n-1, 0, -1):
            c_belt[i][j] = c_belt[i][j-1]
    c_belt[0][0] = temp2
    c_belt[1][0] = temp1
    time += 1
```
#### [코드 2-3]
```python
for i in range(2):
    for j in range(n):
        print(c_belt[i][j], end=' ')
    print()
```
